# Automatização de email - FIXPAY

#USAR PYTHON VERSÃO 3.8#

Programa Criado com o intuito de enviar emails automáticos diariamente , enviando uma senha gerada 


# Como funciona ?

O email loga com o email no campo ['FROM'] = "SEU EMAIL" 

Nos campos: 

username = "EMAIL"

password ="SENHA DO EMAIL"

digite um email e senha válidos para que esse email seja o remetente.


# Definido como email padrão para envio ( temporariamente)


O programa pega a senha do arquivo "senha.txt" então tal pasta terá que ser alterada sempre que houver uma nova pasta 


# Adicionar um novo Email 


O Email do destinatário é salvo na pasta "email_fixay.txt" , todos os email devem ser salvos lá e após cada Email deve haver um " ; "


#OBS - Não importa o tipo de email , gmail , outlook e etc. 


# Executável 


Para baixar o .exe do projeto intale a biblioteca pyinstaller

1 - Entre no terminal de sua IDE  (preferenciamente PYCHARM) e digite : pip install pyinstaller

2 - Ainda no terminal execute o comando pyinstaller Email_FixPay.py 

3 - na pasta dist vai estar seu diretório , agora basta executá-lo e pronto! 





