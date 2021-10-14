
from flask_mail import Mail
from flask import Flask


def init_mail(app: Flask):
    """ Initialises Mail Settings for Flask to use, and recaptcha for the Contact Form"""

    mail_settings = {
        "MAIL_SERVER": 'smtp.gmail.com',
        "MAIL_PORT": 465,
        "MAIL_USE_TLS": False,
        "MAIL_USE_SSL": True,
        "MAIL_USERNAME": 'kaineyb@gmail.com',
        "MAIL_PASSWORD": 'tncykkngaxbblkki'
    }

    app.config.update(mail_settings)

    app.config.update(
        RECAPTCHA_OPTIONS={'theme': 'dark'},

        # Production
        # RECAPTCHA_PUBLIC_KEY="6Lco8qUZAAAAABKxp4jQ_Pp85mNvpeW6XxukMUV1",
        # RECAPTCHA_PRIVATE_KEY="6Lco8qUZAAAAAIgMfgnkFyePIqVsLeft_XTahQP0"


        # Localhost
        RECAPTCHA_PUBLIC_KEY="6Lcw4aUZAAAAADDqdp5nI-DJRM4yeEOE50cJ9kmZ",
        RECAPTCHA_PRIVATE_KEY="6Lcw4aUZAAAAAADZ_dtQzqh9XH1fSrsBOJCNhpv2"


    )

    app.config.from_mapping(
        SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')

    mail = Mail(app)

    return mail
