
from flask_mail import Mail
from flask import Flask

from keys import EMAIL, EMAIL_PASS, PRIVATE, PUBLIC


def init_mail(app: Flask):
    """ Initialises Mail Settings for Flask to use, and recaptcha for the Contact Form"""

    mail_settings = {
        "MAIL_SERVER": 'smtp.gmail.com',
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": EMAIL,
        "MAIL_PASSWORD": EMAIL_PASS
    }

    app.config.update(mail_settings)

    app.config.update(
        RECAPTCHA_DATA_ATTRS = {"theme": "dark", "size": "normal"},

        RECAPTCHA_PUBLIC_KEY=PUBLIC, RECAPTCHA_PRIVATE_KEY=PRIVATE
    )

    app.config.from_mapping(
        SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')

    mail = Mail(app)

    return mail
