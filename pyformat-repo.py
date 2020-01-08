import os
import sys

reponame = sys.argv[1]
repo = f'https://github.com/Zimbani/{reponame}.git'

command = f'git clone {repo} && cd {reponame} && python /home/kai/pyformat.py "*.py" && git add . && git commit -m "Improve readability and PEP 8 compliance" && git push origin master && cd .. && sudo rm -rf {reponame}'
os.system(command)