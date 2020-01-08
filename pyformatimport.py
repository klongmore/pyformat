import sys

import requests

filename = sys.argv[1]
line_count = 0
found = False
import_ = []
working_file = []


def isimportline(line):
    return line.startswith("import ") or line.startswith("from ")


def isbetweenimportlines(line, line_list):
    index = line_list.index(line)
    return isimportline(line_list[index - 1]) and isimportline(line_list[index + 1])


with open(filename, "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        if not found:
            line_count += 1
        if isimportline(line):
            found = True
            if line.startswith("import ") and "," in line:
                comma_split = line[7:].split(",")
                for package in comma_split:
                    fixed_import = f"import {package}"
                    import_.append(fixed_import)
            else:
                import_.append(line)
        elif isbetweenimportlines(line, lines):
            pass
        else:
            working_file.append(line)
import_.sort(key=len)
base_packages = []
pip_packages = []
local_packages = []
for line in import_:
    if line.startswith("import "):
        package = line[7:]
    else:
        package = line.split()[1]
        if "." in package:
            package = package[: package.find(".")]
    baseurl = f"https://docs.python.org/3/library/{package}.html"
    pipurl = f"https://pypi.org/project/{package}/"
    if requests.get(baseurl).status_code == 200:
        base_packages.append(line)
    elif requests.get(pipurl).status_code == 200:
        pip_packages.append(line)
    else:
        local_packages.append(line)
if len(pip_packages) != 0:
    base_packages.append("")
if len(local_packages) != 0:
    pip_packages.append("")
new_imports = base_packages + pip_packages + local_packages
for line in range(len(new_imports)):
    working_file.insert(line + line_count - 1, new_imports[line])
with open(filename, "w") as file:
    for line in working_file:
        file.write(f"{line}\n")
