
class JavaRunner(BaseRunner):

    def __init__(self):
        self.executor = DockerExecutor()

    def execute(self, code: str, stdin: str = ""):

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".java",
            delete=False
        ) as file:

            file.write(code)
            file_path = os.path.abspath(file.name)

        start = time.perf_counter()

        try:

            result = self.executor.run_java(
                file_path,
                stdin
            )

            elapsed = (
                time.perf_counter() - start
            ) * 1000

            if result is None:
                return ExecutionResult(
                    stdout="",
                    stderr="Execution timed out",
                    exit_code=-1,
                    timed_out=True,
                    elapsed_time_ms=round(elapsed, 2)
                )

            return ExecutionResult(
                stdout=result.stdout,
                stderr=result.stderr,
                exit_code=result.returncode,
                timed_out=False,
                elapsed_time_ms=round(elapsed, 2)
            )

        finally:

            if os.path.exists(file_path):
                os.remove(file_path)