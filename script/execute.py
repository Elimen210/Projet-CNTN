import sys
import subprocess
import importlib.util as importlib_util
import os

def installer_django():
    # Installer Django avec pip
    try:
        revelation = subprocess.run(['pip', 'show', 'django'], check=True, text=True)
        print(revelation)
    except revelation == False:
        subprocess.run(["pip", "install", "Django"], check=True, text=True)
        print("Django installé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")


def installer_django_allauth():
    try:
        revelation = subprocess.run(["pip", "show", "django-allauth"], check=True, text=True)
    except revelation == False:
        subprocess.run(["pip", "install", "django-allauth"], check=True, text=True)
        print("django-allauth installé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")
        

def installer_django_crispy():
    try:
        revelation = subprocess.run(["pip", "show", "django-crispy-forms"], check=True, text=True)
    except revelation == False:
        subprocess.run(["pip", "install", "django-crispy-forms"], check=True, text=True)
        print("django-crispy-forms installé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")

        
        
def installer_dotenv():
    try:
        revelation = subprocess.run(["pip", "show", "python-dotenv"], check=True, text=True)
    except revelation == False:
        subprocess.run(["pip", "install", "python-dotenv"], check=True, text=True)
        print("dotenv installé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")
        
def installer_djangorestframework():
    try:
        revelation = subprocess.run(["pip", "show", "djangorestframework"], check=True, text=True)
    except revelation == False:
        subprocess.run(["pip", "install", "djangorestframework"], check=True, text=True)
        print("djangorestframework installé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")
        
def installer_openai():
    try:
        revelation = subprocess.run(["pip", "show", "openai"], check=True, text=True)
    except revelation == False:
        revelation = subprocess.run(["pip", "install", "openai"], check=True, text=True)
        print("openai installé avec succès!")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation : {e}")

if __name__ == "__main__":
    installer_django(), installer_openai(), installer_django_allauth(), installer_django_crispy(), installer_djangorestframework(), installer_dotenv()
    print('Vous avez installé toutes les dépendances du projet')