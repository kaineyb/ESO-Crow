from flask import Flask
from flask_mail import Mail
from keys import keys


def init_mail(app: Flask):
    """Initialises Mail Settings for Flask to use, and recaptcha for the Contact Form"""

    mail_settings = {
        "MAIL_SERVER": "smtp.gmail.com",
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": keys["EMAIL"],
        "MAIL_PASSWORD": keys["EMAIL_PASS"],
    }

    app.config.update(mail_settings)

    app.config.update(
        RECAPTCHA_DATA_ATTRS={"theme": "dark", "size": "normal"},
        RECAPTCHA_PUBLIC_KEY=keys["PUBLIC"],
        RECAPTCHA_PRIVATE_KEY=keys["PRIVATE"],
    )

    mail = Mail(app)

    return mail
