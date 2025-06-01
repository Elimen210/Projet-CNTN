import sys
import subprocess
import os
import shutil
import importlib.util as importlib_util

REQUIRED_PACKAGES = [
    "django",
    "django-allauth",
    "django-crispy-forms",
    "python-dotenv",
    "djangorestframework",
    "openai",
    "requests"
]

def check_python_version(min_major=3, min_minor=6):
    version = sys.version_info
    print(f"Python version détectée : {version.major}.{version.minor}.{version.micro}")
    if (version.major, version.minor) < (min_major, min_minor):
        print(f"? Python {min_major}.{min_minor} ou supérieur est requis.")
        return False
    return True

def create_virtualenv():
    if not os.path.exists("venv"):
        print("?? C
