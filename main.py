import smtplib
import os

# Récupérer le mot de passe à partir d'une variable d'environnement
password = os.getenv('EMAIL_PASSWORD')

# Créer une connexion sécurisée au serveur SMTP de Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  # Commencer TLS pour sécuriser la connexion
server.ehlo()  # S'identifier auprès du serveur

# Authentification
try:
    server.login('walterchristian28@gmail.com', password)
    print("Authentification réussie")
except smtplib.SMTPAuthenticationError:
    print("Erreur d'authentification")
except Exception as e:
    print(f"Erreur : {e}")
finally:
    server.quit()
