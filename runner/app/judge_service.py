import time

from app.executor import Executor
from app.models import (
    JudgeResult,
    TestCaseResult
)
from app.verdict import Verdict


class JudgeService:

    def __init__(self):

        self.executor = Executor()

    def judge(
        self,
        language: str,
        code: str,
        test_cases
    ):

        results = []

        passed_count = 0

        judge_start = time.perf_counter()

        for index, test_case in enumerate(test_cases):

            testcase_start = time.perf_counter()

            execution = self.executor.execute(
                language=language,
                code=code,
                stdin=test_case.input
            )

            testcase_elapsed = (
                time.perf_counter() - testcase_start
            ) * 1000

            actual_output = (
                execution.stdout.strip()
            )

            expected_output = (
                test_case.expected_output.strip()
            )

            if execution.timed_out:

                verdict = Verdict.TIME_LIMIT_EXCEEDED

            elif execution.exit_code != 0:

                verdict = Verdict.RUNTIME_ERROR

            elif actual_output == expected_output:

                verdict = Verdict.ACCEPTED

            else:

                verdict = Verdict.WRONG_ANSWER

            passed = (
                verdict == Verdict.ACCEPTED
            )

            if passed:
                passed_count += 1

            actual_to_return = actual_output
            expected_to_return = expected_output

            if test_case.hidden:

                actual_to_return = None
                expected_to_return = None

            results.append(

                TestCaseResult(
                    testcase_number=index + 1,
                    verdict=verdict,
                    execution_time_ms=round(
                        testcase_elapsed,
                        2
                    ),
                    passed=passed,
                    hidden=test_case.hidden,
                    actual_output=actual_to_return,
                    expected_output=expected_to_return
                )

            )

        overall_verdict = Verdict.ACCEPTED

        for result in results:

            if result.verdict != Verdict.ACCEPTED:

                overall_verdict = result.verdict

                break

        judge_elapsed = (
            time.perf_counter() - judge_start
        ) * 1000

        return JudgeResult(

            verdict=overall_verdict,

            total=len(test_cases),

            passed=passed_count,

            failed=len(test_cases) - passed_count,

            execution_time_ms=round(
                judge_elapsed,
                2
            ),

            results=results
        )