from app import app, mail
from esocrow.models import FeedBackForm
from flask import render_template, request
from flask_mail import Message
from keys import keys


@app.route("/contact", methods=["GET", "POST"])
def registration():
    """
    Checks to see if data is posted or not, if so submits the form and emails
    it to site admin else displays contact form
    """
    form = FeedBackForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        name = form.name.data
        email_address = form.email.data
        feedback = form.feedback.data
        message = form.message.data
        msg = Message(
            f"ESO-Crow: {feedback}",
            sender=(name, email_address),
            reply_to=email_address,
            recipients=[keys["EMAIL"]],
        )
        msg.body = message
        mail.send(msg)

        return render_template("contact/feedback_sent.html")
    return render_template("contact/contact.html", form=form)


@app.route("/feedback_sent")
def email_sent():
    """Returns the template for feedback_sent.html"""
    return render_template("contact/feedback_sent.html")
