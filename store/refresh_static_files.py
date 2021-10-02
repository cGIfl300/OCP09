import subprocess
from sys import executable


def refresh_static_files():
    path_to_python = executable
    shell_stdout = subprocess.run(f"{path_to_python} manage.py collectstatic --noinput", shell=True)
