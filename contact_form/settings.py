
from flask_mail import Mail
from flask import Flask

import os


def keys():

    public = os.environ.get('PUBLIC_KEY')
    private = os.environ.get('PRIVATE_KEY')
    email = os.environ.get('EMAIL_ADDRESS')
    email_pass = os.environ.get('EMAIL_PASSWORD')

    if os.environ.get('LOCAL'):
        print("  ", "*"*20)
        print("   Local Environment Keys Loaded")
        print("  ", "*"*20)

    elif os.environ.get('PRODUCTION'):
        print("  ", "*"*20)
        print("   Production Environment Keys Loaded")
        print("  ", "*"*20)

    else:
        print("Environment Unknown - Keys Not Loaded!")
        public, private, email, email_pass = None, None, None, None

    return public, private, email, email_pass


def init_mail(app: Flask):
    """ Initialises Mail Settings for Flask to use, and recaptcha for the Contact Form"""

    public, private, email, email_pass = keys()

    print("email", email)
    print("email_pass", email_pass)

    mail_settings = {
        "MAIL_SERVER": 'smtp.gmail.com',
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": email,
        "MAIL_PASSWORD": email_pass
    }

    app.config.update(mail_settings)

    app.config.update(
        RECAPTCHA_OPTIONS={'theme': 'dark'},

        RECAPTCHA_PUBLIC_KEY=public, RECAPTCHA_PRIVATE_KEY=private
    )

    app.config.from_mapping(
        SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')

    mail = Mail(app)

    return mail
