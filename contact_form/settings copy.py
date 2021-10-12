from flask_mail import Mail
from flask import Flask

##################
# Instructions
##################

## Rename to settings.py

## Delete the below 2 stings once you've filled out the below.
# Note: SECRET KEY takes a binary string

FILL_ME_OUT = ""
FILL_ME_OUT_BINARY_STRING = b''

##################


def init_mail(app: Flask):
    """ Initialises Mail Settings for Flask to use, and recaptcha for the Contact Form"""

    mail_settings = {
        "MAIL_SERVER": FILL_ME_OUT,
        "MAIL_PORT": FILL_ME_OUT,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": FILL_ME_OUT,
        "MAIL_PASSWORD": FILL_ME_OUT
    }

    app.config.update(mail_settings)

    app.config.update(
        RECAPTCHA_OPTIONS={'theme': 'dark'},

        # Production
        RECAPTCHA_PUBLIC_KEY=FILL_ME_OUT,
        RECAPTCHA_PRIVATE_KEY=FILL_ME_OUT


        # Localhost
        # RECAPTCHA_PUBLIC_KEY=FILL_ME_OUT,
        # RECAPTCHA_PRIVATE_KEY=FILL_ME_OUT


    )

    app.config.from_mapping(
        SECRET_KEY=FILL_ME_OUT_BINARY_STRING)

    mail = Mail(app)

    return mail
