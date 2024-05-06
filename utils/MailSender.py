from email.message import EmailMessage
import smtplib
import os

debug = True


def print_debug(message):
    new_message = "[MailSender.py]: " + message
    if debug:
        print(new_message)


class MailSender():
    def __init__(self):
        self.remitente = os.getenv("REMITENTE")
        self.destinatario = os.getenv("DESTINATARIO")
        self.asunto = os.getenv("ASUNTO")
        self.mensaje = os.getenv("MENSAJE")
        self.clave_correo = os.getenv("CLAVE_CORREO")

        print_debug("Remitente se ha cargado: {}".format(str(self.remitente)))
        print_debug("Destinatario se ha cargado: {}".format(
            str(self.destinatario)))
        print_debug("Asunto se ha cargado: {}".format(str(self.asunto)))
        print_debug("Mensaje se ha cargado: {}".format(str(self.mensaje)))
        print_debug("Clave correo se ha cargado: {}".format(
            str(self.clave_correo)))

    def checkhealth(self):
        return self.clave_correo != None

    def enviar_mensaje(self, nuevo_mensaje):

        self.mensaje = nuevo_mensaje

        email = EmailMessage()
        email["From"] = self.remitente
        email["To"] = self.destinatario
        email["Subject"] = self.asunto
        email.set_content(self.mensaje)

        smtp = smtplib.SMTP_SSL('smtp.gmail.com')
        smtp.login(self.remitente, self.clave_correo)
        smtp.sendmail(self.remitente, self.destinatario, email.as_string())

        print_debug("El mensaje se ha enviado.")

        smtp.quit()


class Test:
    @staticmethod
    def start():
        instance = MailSender()
