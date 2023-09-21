# https://hyunmin1906.tistory.com/276
import smtplib
import ssl

# yiivzpmqbawuzyuz
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "test.zoo0309@gmail.com"
receiver_email = "dev.jhj0309@gmail.com"
password = "yiivzpmqbawuzyuz"
message = "kkk"

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.encode('utf-8'))
