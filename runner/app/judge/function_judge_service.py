import json
import time

from app.languages.registry import LANGUAGES
from app.languages.container_runner import ContainerRunner

from app.models import (
    JudgeResult,
    TestCaseResult
)

from app.verdict import Verdict


class FunctionJudgeService:

    def judge(
        self,
        language: str,
        code: str,
        function_name: str,
        test_cases,
        stop_on_failure=False
    ):

        if language != "python":

            raise ValueError(
                "Function judge currently supports only Python"
            )

        runner_code = self._build_runner(
            code=code,
            function_name=function_name,
            test_cases=test_cases
        )

        config = LANGUAGES[language]

        runner = ContainerRunner(config)

        judge_start = time.perf_counter()

        runner.start(runner_code)

        try:

            execution = runner.execute()

        finally:

            runner.cleanup()

        judge_elapsed = (
            time.perf_counter() - judge_start
        ) * 1000

        if execution.timed_out:

            return JudgeResult(
                verdict=Verdict.TIME_LIMIT_EXCEEDED,
                total=len(test_cases),
                passed=0,
                failed=len(test_cases),
                execution_time_ms=round(
                    judge_elapsed,
                    2
                ),
                results=[]
            )

        if execution.exit_code != 0:

            return JudgeResult(
                verdict=Verdict.RUNTIME_ERROR,
                total=len(test_cases),
                passed=0,
                failed=len(test_cases),
                execution_time_ms=round(
                    judge_elapsed,
                    2
                ),
                results=[]
            )

        raw_results = json.loads(
            execution.stdout
        )

        results = []

        passed_count = 0

        for index, (
            test_case,
            result
        ) in enumerate(
            zip(
                test_cases,
                raw_results
            )
        ):
            
            print(type(result["actual"]))
            print(type(test_case.expected_output))
            print(result["actual"]==test_case.expected_output)

            if not result["success"]:

                verdict = (
                    Verdict.RUNTIME_ERROR
                )

                actual = (
                    result.get("error")
                )

            else:

                actual = result["actual"]

                if (
                    actual
                    ==
                    test_case.expected_output
                ):

                    verdict = (
                        Verdict.ACCEPTED
                    )

                else:

                    verdict = (
                        Verdict.WRONG_ANSWER
                    )

            passed = (
                verdict
                ==
                Verdict.ACCEPTED
            )

            if passed:

                passed_count += 1

            actual_to_return = actual
            expected_to_return = (
                test_case.expected_output
            )

            if test_case.hidden:

                actual_to_return = None
                expected_to_return = None

            results.append(

                TestCaseResult(
                    testcase_number=index + 1,
                    verdict=verdict,
                    execution_time_ms=0,
                    passed=passed,
                    hidden=test_case.hidden,
                    actual_output=(
                        str(actual_to_return)
                        if actual_to_return
                        is not None
                        else None
                    ),
                    expected_output=(
                        str(expected_to_return)
                        if expected_to_return
                        is not None
                        else None
                    )
                )

            )

            if (
                not passed
                and stop_on_failure
            ):

                break

        overall_verdict = (
            Verdict.ACCEPTED
        )

        for result in results:

            if (
                result.verdict
                !=
                Verdict.ACCEPTED
            ):

                overall_verdict = (
                    result.verdict
                )

                break

        return JudgeResult(
            verdict=overall_verdict,
            total=len(results),
            passed=passed_count,
            failed=len(results)
            - passed_count,
            execution_time_ms=round(
                judge_elapsed,
                2
            ),
            results=results
        )

    def _build_runner(
        self,
        code,
        function_name,
        test_cases
    ):

        test_data = [

            {
                "args": tc.args
            }

            for tc in test_cases

        ]

        return f"""
import json

{code}

tests = {json.dumps(test_data)}

solution = Solution()

results = []

for test in tests:

    try:

        actual = getattr(
            solution,
            "{function_name}"
        )(
            *test["args"]
        )

        results.append(
            {{
                "success": True,
                "actual": actual
            }}
        )

    except Exception as e:

        results.append(
            {{
                "success": False,
                "error": str(e)
            }}
        )

print(
    json.dumps(results)
)
"""