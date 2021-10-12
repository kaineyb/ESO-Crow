
""" The hook for the flask app to run """

####################
# Modules
####################

# Built-ins

# Flask


from flask import Flask
from flask_bootstrap import Bootstrap

# 3rd Party

# My stuff
from contact_form.settings import init_mail

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
