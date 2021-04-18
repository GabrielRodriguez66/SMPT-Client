import os
import smtplib, ssl
from email.message import EmailMessage


class EmailMessageFactory:
    @staticmethod
    def get_message(sender, to, subject, content):
        msg = EmailMessage()
        msg['From'] = sender
        msg['To'] = to
        msg['Subject'] = subject
        msg.set_content(content)
        return msg


class SMTPClient:
    def __init__(self, email, password, smtp_server):
        self.email = email
        self.password = password
        self.smtp_server = smtp_server

    def send_email(self, to, subject, content):
        msg = EmailMessageFactory.get_message(self.email, to, subject, content)
        with smtplib.SMTP_SSL(self.smtp_server, 465, context=ssl.create_default_context()) as server:
            print("Starting login...")
            server.login(self.email, self.password)
            print("Sending email...")
            server.send_message(msg)
            print("Email sent successfully!")


if __name__ == '__main__':
    client = SMTPClient(email=os.environ.get('EMAIL'), password=os.environ.get('EMAIL_PWD'), smtp_server="smtp.gmail.com")
    client.send_email(to="", subject="SMTP Testing", content="Hi there, this message is from Python.")
