import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

senha = open('senha.txt', 'r')
senha = senha.read()

email = open('email_fixpay.txt', 'r')
email = email.read()
print('Criando mensagem...')

username = "kevenmatheus.fixpay@gmail.com"
password = "88490255"
mail_from = "kevenmatheus.fixpay@gmail.com"
mail_to = email
mail_subject = "Senha diaria FixPay"


mail_body_html = f"""

   Olá! , aqui é a FixPay.


   Segue Abaixo sua senha diaria :

         {senha}
 
 Atenciosamente,
 
 FIXPAY DESENVOLVIMENTO

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