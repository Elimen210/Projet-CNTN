import sys
import subprocess
import importlib.util as importlib_util
import os

def installer_django():
    """Installe Django automatiquement avec un environnement virtuel."""

    # 2. Activer l'environnement virtuel
    # (Les commandes varient selon le syst�me d'exploitation)
    if os.name == 'nt':  # Windows
        os.system(".\venv\Scripts\activate")
    else:  # Linux/macOS
        os.system("source venv/bin/activate")

    # 3. Installer Django avec pip
    try:
        subprocess.run(["pip", "install", "Django"], check=True, text=True)
        print("Django install� avec succ�s!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")

    # 4. (Optionnel) Cr�er un nouveau projet Django
    # Remplacez "mon_projet" par le nom de votre projet
    try:
        subprocess.run(["django-admin", "startproject", "mon_projet"], check=True, text=True)
        print("Projet Django cr�� avec succ�s!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la cr�ation du projet : {e}")

if __name__ == "__main__":
    installer_django()

def installer_django_allauth():
    try:
        subprocess.run(["pip", "install", "django-allauth"], check=True, text=True)
        print("django-allauth install� avec succ�s!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")
        

def installer_django_crispy():
    try:
        subprocess.run(["pip", "install", "django-crispy-forms"], check=True, text=True)
        print("django-crispy-forms install� avec succ�s!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")

        
        
def installer_dotenv():
    try:
        subprocess.run(["pip", "install", "python-dotenv"], check=True, text=True)
        print("dotenv install� avec succ�s!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")
        
def installer_djangorestframework():
    try:
        subprocess.run(["pip", "install", "djangorestframework"], check=True, text=True)
        print("djangorestframework install� avec succ�s!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")
        
def installer_openai():
    try:
        subprocess.run(["pip", "install", "openai"], check=True, text=True)
        print("openai install� avec succ�s!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")

if __name__ == "__main__":
    installer_django(), installer_openai(), installer_django_allauth(), installer_django_crispy(), installer_djangorestframework(), installer_dotenv()