from pydantic import BaseModel


class ExecuteRequest(BaseModel):
    language: str = "python"
    code: str
    stdin: str = ""


class ExecutionResult(BaseModel):
    stdout: str
    stderr: str
    exit_code: int
    timed_out: bool
    elapsed_time_ms: float

from dataclasses import dataclass


@dataclass
class DockerExecutionResult:
    stdout: str
    stderr: str
    returncode: int
    timed_out: bool

class ErrorResponse(BaseModel):
    error: str