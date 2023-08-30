import secrets
import string
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())



def generate_confirmation_token():
    """ Генерируем случайный токен, состоящий из букв и цифр """
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(32))
    return token


def send_confirmation_email(email, confirmation_token):
    subject = "Подтверждение регистрации"
    message = f"Для завершения регистрации, перейдите по ссылке: http://127.0.0.1:8000/confirm/{confirmation_token}"

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = os.getenv('SMTP_USERNAME')
    msg['To'] = email

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, [email], msg.as_string())
        print("Письмо с подтверждением отправлено")
    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")
