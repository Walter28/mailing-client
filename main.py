import smtplib
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# Récupérer le mot de passe à partir d'une variable d'environnement
password = os.getenv('EMAIL_PASSWORD')

# Vérifier si la variable d'environnement est définie
if not password:
    raise ValueError("Erreur : la variable d'environnement EMAIL_PASSWORD n'est pas définie")

# Créer une connexion sécurisée au serveur SMTP de Gmail
server = smtplib.SMTP('smtp.gmail.com', (587))
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
    
    
# Création de l'objet MIMEMultipart pour le message
msg = MIMEMultipart()
msg['From'] = 'walter'
msg['To'] = 'kovojop649@bacaki.com'  # fake 10min mailbox
msg['Subject'] = 'Just a test'

# Lecture du contenu du message
with open('message.txt', 'r') as f:
    message = f.read()

# Attacher le contenu du message en tant que texte brut
msg.attach(MIMEText(message, 'plain'))

# Gestion de la pièce jointe
filename = 'image_attach.jpg'
attachment = open(filename, 'rb')

# Création d'un objet MIMEBase pour la pièce jointe
p = MIMEBase('application', 'octet_stream')
p.set_payload(attachment.read())

# Encodage et ajout des en-têtes de la pièce jointe
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachement; filename={filename}')
msg.attach(p)

# Conversion du message en chaîne et envoi de l'email
text = msg.as_string()
server.sendmail('walterchristian28@gmail.com', 'kovojop649@bacaki.com', text)

# Fermeture de la connexion au serveur SMTP
server.quit()