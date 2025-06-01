import sys
import subprocess
import importlib.util as importlib_util
import os

class PythonConfiguration:
    @classmethod
    def Validate(cls):
        if not cls.__ValidatePython():
            return # cannot validate further

        for packageName in ["requests"]:
            if not cls.__ValidatePackage(packageName):
                return # cannot validate further

    @classmethod
    def __ValidatePython(cls, versionMajor = 3, versionMinor = 3):
        if sys.version is not None:
            print("Python version {0:d}.{1:d}.{2:d} detected.".format( \
                sys.version_info.major, sys.version_info.minor, sys.version_info.micro))
            if sys.version_info.major < versionMajor or (sys.version_info.major == versionMajor and sys.version_info.minor < versionMinor):
                print("Python version too low, expected version {0:d}.{1:d} or higher.".format( \
                    versionMajor, versionMinor))
                return False
            return True

    @classmethod
    def __ValidatePackage(cls, packageName):
        if importlib_util.find_spec(packageName) is None:
            return cls.__InstallPackage(packageName)
        return True

    @classmethod
    def __InstallPackage(cls, packageName):
        permissionGranted = False
        while not permissionGranted:
            reply = str(input("Would you like to install Python package '{0:s}'? [Y/N]: ".format(packageName))).lower().strip()[:1]
            if reply == 'n':
                return False
            permissionGranted = (reply == 'y')
        
        print(f"Installing {packageName} module...")
        subprocess.check_call(['python', '-m', 'pip', 'install', packageName])

        return cls.__ValidatePackage(packageName)

if __name__ == "__main__":
    PythonConfiguration.Validate()

def installer_django():
    """Installe Django automatiquement avec un environnement virtuel."""

    # 2. Activer l'environnement virtuel
    # (Les commandes varient selon le système d'exploitation)
    if os.name == 'nt':  # Windows
        os.system(".\venv\Scripts\activate")
    else:  # Linux/macOS
        os.system("source venv/bin/activate")

    # 3. Installer Django avec pip
    try:
        subprocess.run(["pip", "install", "Django"], check=True, text=True)
        print("Django installé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")

    # 4. (Optionnel) Créer un nouveau projet Django
    # Remplacez "mon_projet" par le nom de votre projet
    try:
        subprocess.run(["django-admin", "startproject", "mon_projet"], check=True, text=True)
        print("Projet Django créé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la création du projet : {e}")

if __name__ == "__main__":
    installer_django()

def installer_django_allauth:
    try:
        subprocess.run(["pip", "install", "django-allauth"], check=True, text=True)
        print("django-allauth installé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")
        

def installer_django_crispy-forms:
    try:
        subprocess.run(["pip", "install", "django-crispy-forms"], check=True, text=True)
        print("django-crispy-forms installé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")
        
        
def installer_python-dotenv:
    try:
        subprocess.run(["pip", "install", "python-dotenv"], check=True, text=True)
        print("dotenv installé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")
        
def installer_djangorestframework:
    try:
        subprocess.run(["pip", "install", "djangorestframework"], check=True, text=True)
        print("djangorestframework installé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")
        
def installer_openai:
    try:
        subprocess.run(["pip", "install", "openai"], check=True, text=True)
        print("openai installé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")