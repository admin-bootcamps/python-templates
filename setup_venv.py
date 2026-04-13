"""
Sets up a Python virtual environment and installs dependencies.
Run this script from the project root folder:

    python setup_venv.py

Only requires Python (no other tools needed).
"""

import os
import subprocess
import sys
import venv

VENV_DIR = ".venv"


def venv_exists():
    return os.path.isfile(os.path.join(VENV_DIR, "pyvenv.cfg"))


def create_venv():
    if venv_exists():
        print(f"Virtual environment already exists in '{VENV_DIR}', skipping creation.")
        return
    print(f"Creating virtual environment in '{VENV_DIR}'...")
    venv.create(VENV_DIR, with_pip=True)
    print("Virtual environment created.")


def get_pip_path():
    if sys.platform == "win32":
        return os.path.join(VENV_DIR, "Scripts", "pip.exe")
    return os.path.join(VENV_DIR, "bin", "pip")


def install_requirements():
    pip = get_pip_path()
    if not os.path.exists("requirements.txt"):
        print("No requirements.txt found, skipping package install.")
        return
    print("Installing packages from requirements.txt...")
    subprocess.check_call([pip, "install", "-r", "requirements.txt"])
    print("Packages installed.")


def print_activation_instructions():
    print()
    print("Setup complete! To activate the virtual environment, run:")
    if sys.platform == "win32":
        cmd_activate = os.path.join(VENV_DIR, "Scripts", "activate")
        powershell_activate = os.path.join(".", VENV_DIR, "Scripts", "Activate.ps1")
        print("  In Command Prompt (cmd.exe):")
        print(f"    {cmd_activate}")
        print("  In PowerShell:")
        print(f"    {powershell_activate}")
    else:
        activate_path = os.path.join(VENV_DIR, "bin", "activate")
        print(f"    source {activate_path}")


if __name__ == "__main__":
    create_venv()
    install_requirements()
    print_activation_instructions()
