import os
import time
import tempfile
import subprocess

from app.config import CONFIG
from app.languages.base_runner import BaseRunner
from app.models import ExecutionResult


class PythonRunner(BaseRunner):

    def execute(self, code: str, stdin: str = ""):

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False
        ) as file:

            file.write(code)
            file_path = file.name

        try:

            start = time.perf_counter()

            result = subprocess.run(
                ["python", file_path],
                input=stdin,
                capture_output=True,
                text=True,
                timeout=CONFIG.timeout_seconds
            )

            elapsed = (time.perf_counter() - start) * 1000

            return ExecutionResult(
                stdout=result.stdout[:CONFIG.max_output_size],
                stderr=result.stderr[:CONFIG.max_output_size],
                exit_code=result.returncode,
                timed_out=False,
                elapsed_time_ms=round(elapsed, 2)
            )

        except subprocess.TimeoutExpired:

            return ExecutionResult(
                stdout="",
                stderr="Execution timed out",
                exit_code=-1,
                timed_out=True,
                elapsed_time_ms=CONFIG.timeout_seconds * 1000
            )

        finally:
            if os.path.exists(file_path):
                os.remove(file_path)