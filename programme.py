'''
Application de compte à rebours automatique par mails

               fait par Nathan BOSY
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import time

'''
VARIABLES A REMPLIR !
'''
#          Minute   Heure     Jour       Mois     Année
objectif = [0,       17,       12,       4,       2023]

sujet = 'Ceci est le sujet du message !'

corps = 'Ceci est le corps du message.\nCordialement.'

destinataires = [   'mail1@gmail.com',
                    'mail2@gmail.com',
                    'mail3@gmail.com']

votre_mail = 'monmails@outlook.com'

votre_mdp =  '*******'

attente_entre_mails = 600 # en secondes



'''
Fonction qui envoie les mails
'''
def envoi(destinataires, sujet, corps, expediteurs, mot_de_passe):
    try:
        smtp_server = "smtp-mail.outlook.com" # Pour les adresses outlook
        port = 587
        destinataires = ", ".join(destinataires)

        message = MIMEMultipart()
        message['From'] = expediteurs
        message['To'] = destinataires
        message['Subject'] = sujet
        message.attach(MIMEText(corps, 'plain'))

        smtp_obj = smtplib.SMTP(smtp_server, port)
        smtp_obj.starttls()
        smtp_obj.login(expediteurs, mot_de_passe)

        smtp_obj.sendmail(expediteurs, destinataires, message.as_string())
        smtp_obj.quit()
        print("Envoi effectué !")
    except Exception as e:
        print("[ERREUR]  - ", e)



'''
Fonction qui calcule le temps restant
'''    
def temps_restant():
    maintenant = datetime.datetime.now()
    date_cible = datetime.datetime(objectif[4], objectif[3], objectif[2], objectif[1], objectif[0])
    difference = date_cible - maintenant
    if maintenant >= date_cible :
        return "Temps écoulé !"    

    jours_restants = difference.days
    heures_restantes, remainder = divmod(difference.seconds, 3600)
    minutes_restantes, _ = divmod(remainder, 60)
    temps = (jours_restants, heures_restantes, minutes_restantes)

    return "Temps restant : {} heures et {} minutes \n".format(temps[1], temps[2])



while True:
    envoi(destinataires, sujet, temps_restant(), votre_mail, votre_mdp)
    time.sleep(600)