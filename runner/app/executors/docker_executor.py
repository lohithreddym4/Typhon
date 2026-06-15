import subprocess


class DockerExecutor:

    def run(
        self,
        image: str,
        code_path: str,
        run_command: list[str],
        stdin: str = ""
    ):

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
            image,
            *run_command
        ]

        try:

            return subprocess.run(
                command,
                input=stdin,
                capture_output=True,
                text=True,
                timeout=5
            )

        except subprocess.TimeoutExpired:

            return None