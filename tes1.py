import openai

def test_key(api_key):
    openai.api_key = "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"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}]
        )
        print("✅ Clé valide:", api_key[:15] + "...")
        print("Réponse:", response.choices[0].message['content'])
    except openai.error.AuthenticationError:
        print("❌ Clé invalide:", api_key[:15] + "...")
    except openai.error.RateLimitError:
        print("⚠️ Clé valide mais quota dépassé:", api_key[:15] + "...")
    except Exception as e:
        print("⚠️ Autre erreur:", api_key[:15] + "...", str(e))

# Exemple d’appel
test_key("sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")