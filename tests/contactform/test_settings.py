
from flask_mail import Mail
from flask import Flask

from contact_form.settings import init_mail


def test_settings():
    """ Checks the link isn't broken. """

    assert init_mail


def test_init_mail():

    app = Flask(__name__)

    assert isinstance(app, Flask)

    app = init_mail(app)

    assert isinstance(app, Mail)
