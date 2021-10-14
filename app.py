
""" The hook for the flask app to run """

####################
# Modules
####################

# Built-ins

# Flask
from contact_form.settings import init_mail
from flask_bootstrap import Bootstrap
from flask import Flask

# 3rd Party

# My stuff

####################
# App
####################

app = Flask(__name__)

bootstrap = Bootstrap(app)

mail = init_mail(app)

####################
# Routes (Needs to be called last see: https://flask.palletsprojects.com/en/2.0.x/patterns/packages/
####################
import routes.all  # noqa
