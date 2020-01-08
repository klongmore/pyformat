import os
import sys

arg = sys.argv[1]
command = f"black {arg} &> /dev/null && autopep8 --in-place --aggressive --aggressive {arg} && black {arg} &> /dev/null"
os.system(command)

if arg == "*.py":
    for file in os.listdir("."):
        if file.endswith(".py"):
            command = f"python /home/kai/pyformatimport.py {file}"
            os.system(command)
elif arg.endswith(".py"):
    command = f"python /home/kai/pyformatimport.py {arg}"
    os.system(command)

command = f"black {arg}"
os.system(command)
