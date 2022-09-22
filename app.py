""" The hook for the flask app to run """

####################
# Modules
####################

# Built-ins

import os

from flask import Flask
from flask_bootstrap import Bootstrap4

# Flask
from contact_form.settings import init_mail

# 3rd Party

# My stuff

####################
# App
####################

app = Flask(__name__)

# app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

bootstrap = Bootstrap4(app)

mail = init_mail(app)

####################
# Routes (Needs to be called last see: https://flask.palletsprojects.com/en/2.0.x/patterns/packages/
####################
import routes.all  # noqa
