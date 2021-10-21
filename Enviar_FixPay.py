import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

senha = open('senha.txt', 'r')
senha = senha.read()

email = open('email_fixpay.txt', 'r')
email = email.read()
print('Criando mensagem...')

username = "EMAIL"
password = "SENHA DO EMAIL "
mail_from = "EMAIL DO REMETENTE"
mail_to = email
mail_subject = "Senha diaria"


mail_body_html = f"""

   Olá! , aqui é a 


   Segue Abaixo sua senha diaria :

         {senha}
 
 Atenciosamente,
 

"""

mimemsg = MIMEMultipart()
mimemsg['From'] = mail_from
mimemsg['To'] = mail_to
mimemsg['Subject'] = mail_subject

print('Adicionando texto...')

mimemsg.attach(MIMEText(mail_body_html, 'plain'))
connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
connection.starttls()
connection.login(username, password)

print('Enviando mensagem...')

connection.send_message(mimemsg)

print('Mensagem enviada...')

connection.quit()
