import subprocess


class DockerExecutor:

    def run_python(self, code_path: str,stdin: str = "") -> subprocess.CompletedProcess | None:

        command = [
            "docker",
            "run",
            "--rm",
            "--network", "none",
            "--memory", "128m",
            "--cpus", "1",
            "--pids-limit", "64",
            "-i",
            "-v", f"{code_path}:/sandbox/main.py:ro",
            "typhon-python",
            "python",
            "/sandbox/main.py"
        ]

        try:

            return subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=5,
                input=stdin
            )

        except subprocess.TimeoutExpired:

            return None