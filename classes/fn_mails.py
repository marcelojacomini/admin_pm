from data_base.data_base import Con
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class Mails:
    def __init__(self):
        self.password = None
        self.msg_from = None
        self.mail_smtp = None

        cnx = Con().con()

        with cnx.cursor() as c:
            c.execute(f"SELECT * FROM fn_mail")
            mail_1 = c.fetchone()
            self.password = mail_1['password']
            self.msg_from = mail_1['msg_from']
            self.mail_smtp = mail_1['mail_smtp']

    def send_mail(self, msg_to, msg_subject, message):
        # create message object instance
        msg = MIMEMultipart()
        # message = "Teste Python Admin_PM"

        # set the parameters of the message
        password = self.password
        msg['From'] = self.msg_from
        msg['To'] = msg_to
        msg['Subject'] = msg_subject

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # create server
        server = smtplib.SMTP(self.mail_smtp)
        # server.starttls()

        # Login Credentials for sending the mail
        server.login(msg['From'], password)

        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

        print("successfully sent email to %s:" % (msg['To']))


def insert_mail(password, msg_from, mail_smtp):
    cnx = Con().con()
    with cnx.cursor() as c:
        c.execute("SELECT * FROM fn_mail")
        if c.fetchone():
            c.execute(f"UPDATE fn_mail SET password = '{password}', "
                      f"msg_from = '{msg_from}', mail_smtp = '{mail_smtp}' "
                      f"WHERE id_mail = {1}")

            cnx.commit()
        else:
            c.execute(f"INSERT INTO fn_mail (password, msg_from, mail_smtp) VALUES "
                      f"('{password}', '{msg_from}', '{mail_smtp}')")
            cnx.commit()
