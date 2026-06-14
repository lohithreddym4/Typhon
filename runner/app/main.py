from fastapi import FastAPI
from app.models import (
    ExecuteRequest,
    ExecutionResult
)


from app.executor import Executor


app = FastAPI()

executor = Executor()


@app.post(
    "/execute",
    response_model=ExecutionResult
)
def execute(req: ExecuteRequest):

    return executor.execute(
        language=req.language,
        code=req.code,
        stdin=req.stdin
    )