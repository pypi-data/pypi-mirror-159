from os import system

class start:
    mkdir = input("Name of your package : ")
    system("mkdir src")
    system("cd src")
    system("mkdir .\src" + f"\{mkdir}")
    system("cd " + mkdir)
    system("echo 'WTH' > src" + f"\{mkdir}\__init__.py")
    system("echo your license > LICENSE")
    system("echo # Readme.md > README.md")
    system('echo https://packaging.python.org/en/latest/tutorials/packaging-projects/#codecell9> pyproject.toml')
    system("py -m pip install .")