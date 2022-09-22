""" The hook for the flask app to run """

####################
# Modules
####################

# Built-ins

from flask import Flask
from flask_bootstrap import Bootstrap

# Flask
from contact_form.settings import init_mail
from keys import S_KEY

# 3rd Party

# My stuff

####################
# App
####################

app = Flask(__name__)

app.config["SECRET_KEY"] = S_KEY

bootstrap = Bootstrap(app)

mail = init_mail(app)

####################
# Routes (Needs to be called last see: https://flask.palletsprojects.com/en/2.0.x/patterns/packages/
####################
import routes.all  # noqa
