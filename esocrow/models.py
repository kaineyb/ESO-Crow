# model.py
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import SubmitField, StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length


class FeedBackForm(FlaskForm):
    name = StringField('Name',
                       [DataRequired()])
    email = StringField('Email Address', [DataRequired(),
                                          Email(granular_message=True, check_deliverability=True), Length(min=6, max=35, message="Email needs to be between 6 and 35 characters")])

    feedback = SelectField('Feedback type', choices=[
        ('General Feedback', 'General Feedback'),
        ('New Location', 'New Location'),
        ('Found a Bug/Error', 'Found a Bug/Error')
    ])

    message = TextAreaField('Message', [DataRequired(), Length(
        min=10, message="Please enter a message of at least 10 characters")])

    recaptcha = RecaptchaField()

    submit = SubmitField('Submit')
