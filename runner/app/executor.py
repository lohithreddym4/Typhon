from app.languages.python_runner import PythonRunner
from fastapi import HTTPException

class Executor:

    def __init__(self):

        self.runners = {
            "python": PythonRunner()
        }

    def execute(
        self,
        language: str,
        code: str,
        stdin: str = ""
    ):

        # runner = self.runners.get(language)

        # if not runner:
        #     raise ValueError(
        #         f"Unsupported language: {language}"
        #     )
        runner = self.runners.get(language)

        if not runner:
            raise HTTPException(
            status_code=400,
            detail=f"Unsupported language: {language}"
            )

        return runner.execute(
            code=code,
            stdin=stdin
        )