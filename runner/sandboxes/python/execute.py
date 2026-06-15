import sys

code_file = sys.argv[1]

with open(code_file, "r") as f:
    code = f.read()

exec(code)