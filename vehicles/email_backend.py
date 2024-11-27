from django.core.mail.backends.smtp import EmailBackend
import ssl

class CustomEmailBackend(EmailBackend):
    def open(self):
        self.connection = super().open()
        if self.connection and not self.use_ssl:
            # Wrap the connection in an unverified SSL context
            self.connection.starttls(context=ssl._create_unverified_context())
        return self.connection
