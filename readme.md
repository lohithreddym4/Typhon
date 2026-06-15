# Typhon

A secure, container-based code execution engine built with FastAPI and Docker.

Typhon executes untrusted code inside isolated Docker containers while enforcing strict resource limits and security controls.

Repository:

https://github.com/lohithreddym4/Typhon

---

## Features

* Python code execution
* Docker sandboxing
* Standard input (stdin) support
* Execution timeouts
* Network isolation
* Memory limits
* PID limits
* Filesystem isolation
* Language abstraction architecture
* Execution metrics

---

## Why Typhon?

Most online judges focus on execution.

Typhon focuses on execution **and isolation**.

Every submission runs inside its own temporary container with:

* No internet access
* Limited memory
* Limited CPU resources
* Limited process creation
* Automatic cleanup

---

## Quick Start

### Clone

```bash
git clone https://github.com/lohithreddym4/Typhon.git

cd Typhon/runner
```

### Create Virtual Environment

Windows:

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv .venv

source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Build Python Sandbox

```bash
docker build -t fedjudge-python ./sandboxes/python
```

### Run API

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Example Request

```json
{
  "language": "python",
  "code": "print('Hello Typhon')"
}
```

Response:

```json
{
  "stdout": "Hello Typhon\n",
  "stderr": "",
  "exit_code": 0,
  "timed_out": false
}
```

---

## Security Model

Each submission is executed using:

```text
docker run
    --rm
    --network none
    --memory 128m
    --cpus 1
    --pids-limit 64
```

Current protections:

* Network isolation
* Memory exhaustion protection
* Infinite loop timeout protection
* Process explosion protection
* Non-root execution
* Temporary container execution

---

## Current Status

### Sprint 1

* Python execution
* stdin support
* timeout support
* execution metrics

### Sprint 2

* Dockerized execution
* network isolation
* memory limits
* PID limits
* filesystem isolation

### Sprint 3 (Next)

* Java runner
* Java compilation
* Java sandbox image

---

## Vision

Typhon aims to become a language-agnostic execution platform for:

* Coding assessment systems
* Online IDEs
* Learning platforms
* Competitive programming platforms
* AI-powered coding products

Execute Anything. Contain Everything.
