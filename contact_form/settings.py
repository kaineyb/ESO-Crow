from flask import Flask
from flask_mail import Mail
from keys import EMAIL, EMAIL_PASS, PRIVATE, PUBLIC, SECRET_KEY


def init_mail(app: Flask):
    """Initialises Mail Settings for Flask to use, and recaptcha for the Contact Form"""

    mail_settings = {
        "MAIL_SERVER": "smtp.gmail.com",
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": EMAIL,
        "MAIL_PASSWORD": EMAIL_PASS,
    }

    app.config.update(mail_settings)

    app.config.update(
        RECAPTCHA_DATA_ATTRS={"theme": "dark", "size": "normal"},
        RECAPTCHA_PUBLIC_KEY=PUBLIC,
        RECAPTCHA_PRIVATE_KEY=PRIVATE,
    )

    app.config.from_mapping(SECRET_KEY=SECRET_KEY)

    mail = Mail(app)

    return mail
