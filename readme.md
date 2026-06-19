# Typhon

Typhon is a secure, container-based online judge engine built with FastAPI and Docker.

Unlike traditional code execution services, Typhon is designed to evaluate user submissions against test cases, generate verdicts, and support complex language-specific structures such as TreeNode, ListNode, custom objects, collections, and overloaded methods.

Built from frustration with Judge0.

**Execute anything. Judge everything.**

---

## Features

### Languages

Currently supported:

* Python 3
* Java 21

Additional languages can be added through Typhon's language registry.

---

## Judge Engine

Typhon supports function-based judging similar to LeetCode and HackerRank.

Features:

* Multiple test cases per submission
* Single execution for all test cases
* Verdict generation
* Execution time measurement
* Hidden test cases
* Stop-on-failure mode
* Runtime error detection
* Compilation error detection
* Time limit exceeded detection

Supported verdicts:

* ACCEPTED
* WRONG_ANSWER
* RUNTIME_ERROR
* COMPILATION_ERROR
* TIME_LIMIT_EXCEEDED

---

## Advanced Java Support

Typhon automatically handles:

### Primitive Types

* int
* long
* double
* float
* boolean
* char
* String

### Arrays

* int[]
* long[]
* String[]
* int[][]
* nested arrays

### Collections

* List<T>
* Set<T>
* Map<K,V>
* Nested collections

Examples:

```java
List<Integer>
List<List<Integer>>
Map<String,Integer>
Set<Long>
```

### Linked Structures

Typhon automatically serializes and deserializes:

```java
ListNode
TreeNode
```

Examples:

```text
[1,2,3,4]
```

→ ListNode

```text
[1,null,2,3]
```

→ TreeNode

### Custom Objects

Example:

```java
class Point {
    int x;
    int y;
}
```

Input:

```json
{
  "x": 3,
  "y": 4
}
```

Output:

```json
{
  "x": 3,
  "y": 4
}
```

### Method Overloading

Typhon supports overloaded methods through explicit type hints.

Example:

```java
int add(int a, int b)

String add(String a, String b)
```

---

## Python Support

Typhon supports:

### Function Style

```python
def square(n):
    return n * n
```

### Solution Class Style

```python
class Solution:

    def square(self, n):
        return n * n
```

---

## Security

Every execution runs inside an isolated Docker container.

Sandbox restrictions:

```text
--network none
--memory 256m
--cpus 1
```

Security guarantees:

* Network isolation
* Resource limits
* Container cleanup
* Process isolation
* Untrusted code execution

---

## Architecture

```text
Client
  │
  ▼
Judge API
  │
  ▼
Build Runner
  │
  ▼
Language Runner
  │
  ▼
Docker Sandbox
  │
  ▼
Result Parser
  │
  ▼
Verdict Generator
```

---

## Installation

### Requirements

* Python 3.11+
* Docker Desktop
* Git

Verify installation:

```bash
python --version
docker --version
git --version
```

---

### Clone Repository

```bash
git clone https://github.com/lohithreddym4/Typhon.git

cd Typhon/runner
```

---

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

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Build Sandbox Images

```bash
python scripts/build_sandboxes.py
```

Verify:

```bash
docker images
```

Expected:

```text
typhon-python
typhon-java
```

---

### Run Typhon

```bash
uvicorn app.main:app --reload
```

Swagger:

```text
http://localhost:8000/docs
```

---

## Function Judge Example

Endpoint:

```http
POST /judge/function
```

Example:

```json
{
  "language": "python",
  "function_name": "square",
  "code": "def square(n): return n*n",
  "test_cases": [
    {
      "args": [5],
      "expected_output": 25
    }
  ]
}
```

Response:

```json
{
  "verdict": "ACCEPTED",
  "total": 1,
  "passed": 1,
  "failed": 0
}
```

---

## Performance

Benchmark (local machine):

```text
1 testcase      ≈ 3.2s
10 testcases    ≈ 3.2s
100 testcases   ≈ 3.2s
1000 testcases  ≈ 3.4s
```

Typhon executes all test cases within a single sandbox execution, minimizing interpreter startup overhead.

---

## Current Status

Typhon v1.0

Implemented:

* Python Judge
* Java Judge
* Docker Sandboxing
* Function Evaluation
* Verdict Generation
* TreeNode Support
* ListNode Support
* Custom Objects
* Collections
* Overload Resolution
* Timeout Detection
* Concurrency Validation

Future:

* Submission Queue
* Persistent Workers
* Additional Languages
* Distributed Execution
* Contest Support

---

Built because online judges should be extensible, language-aware, and easy to own.

**Execute anything. Judge everything.**
