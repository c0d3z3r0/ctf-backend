"""SMTP email backend class."""
import smtplib

from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend as BaseEmailBackend
from django.core.mail.message import sanitize_address

from dynamic_preferences.registries import \
    global_preferences_registry as dynprefs

prefs = dynprefs.manager()


# Override Mail backend to use dynprefs
class EmailBackend(BaseEmailBackend):

    def __init__(self, host=None, port=None, username=None, password=None,
                 **kwargs):
        super().__init__(host, port, username, password, **kwargs)
        self.host = host or prefs['mail__smtp_host']
        self.port = port or prefs['mail__smtp_port']
        self.username = password or prefs['mail__smtp_user']
        self.password = password or prefs['mail__smtp_password']

    def _send(self, email_message):
        if not email_message.recipients():
            return False

        return_path = sanitize_address(prefs['mail__return_path'],
                                       email_message.encoding)
        recipients = [sanitize_address(addr, email_message.encoding)
                      for addr in email_message.recipients()]

        if email_message.from_email == settings.DEFAULT_FROM_EMAIL:
            email_message.from_email = prefs['mail__return_path']
        if not 'From' in email_message.extra_headers:
            email_message.extra_headers['From'] = prefs['mail__from']

        message = email_message.message()

        try:
            self.connection.sendmail(return_path, recipients,
                                     message.as_bytes(linesep='\r\n'))
        except smtplib.SMTPException:
            if not self.fail_silently:
                raise
            return False
        return True
