import string
from model import FeedBackForm
from flask import Flask, request, redirect, render_template
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap
from random import choice

# My stuff:
import eso_crow


# TODO Feedback form! Lets look into Flask-WTF, for security and feedback form.

app = Flask(__name__)

bootstrap = Bootstrap(app)

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

    # Live
    RECAPTCHA_PUBLIC_KEY="6Lco8qUZAAAAABKxp4jQ_Pp85mNvpeW6XxukMUV1",
    RECAPTCHA_PRIVATE_KEY="6Lco8qUZAAAAAIgMfgnkFyePIqVsLeft_XTahQP0"


    # Localhost
    # RECAPTCHA_PUBLIC_KEY="6Lcw4aUZAAAAADDqdp5nI-DJRM4yeEOE50cJ9kmZ",
    # RECAPTCHA_PRIVATE_KEY="6Lcw4aUZAAAAAADZ_dtQzqh9XH1fSrsBOJCNhpv2"


)

app.config.from_mapping(
    SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')

mail = Mail(app)

# TODO - Look at handle_email and handle_data as they produce an error when viewed in browser


@app.route('/contact', methods=['GET', 'POST'])
def registration():
    form = FeedBackForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        email_address = form.email.data
        feedback = form.feedback.data
        message = form.message.data
        msg = Message(f"ESO-Crow: {feedback}", sender=(name, email_address), reply_to=email_address,
                      recipients=["kaineyb@gmail.com"])
        msg.body = message
        mail.send(msg)

        return redirect('/feedback_sent')
    return render_template('contact.html', form=form)


@ app.route('/feedback_sent')
def email_sent():
    return render_template('feedback_sent.html')


@ app.route('/')
def index():
    return render_template('index.html', locations=eso_crow.locations)


@ app.route('/updates')
def updates():
    return render_template('updates.html')


@ app.route('/tip')
def tip():
    return render_template('tip.html')


@ app.route('/faq')
def faq():
    return render_template('faq.html')


@ app.route('/locations')
def get_locations():
    return render_template('locations.html', locations=eso_crow.locations)


@ app.route('/zones')
def get_zones():
    return render_template('zones.html', zones=eso_crow.list_for_zones)


@ app.route('/handle_data', methods=['POST'])
def handle_data():
    source = request.form['source']
    target = request.form['destination']

    if len(source) > 0 and len(target) == 0:
        url = redirect('/' + source)

    elif len(source) > 0 and len(target) > 0:
        url = redirect('/' + source + '/' + target)

    else:
        url = redirect('/')
    return url


@ app.errorhandler(404)
def page_not_found():
    return render_template('page_not_found.html'), 404


@ app.route('/<node>')
def node_page(node):
    node = eso_crow.convert_space(node)

    result = eso_crow.get_node_routes(node)

    how_to_get_to = eso_crow.how_to_get_to(node)

    node = string.capwords(node)

    node = eso_crow.is_stros_mkai(node)

    if isinstance(result, dict):
        return render_template('node.html', node=node, edges=result, how_to_get_to=how_to_get_to)

    else:
        return render_template('page_not_found.html'), 404


@ app.route('/<source>/<target>')
def dijkstra(source, target):
    source = eso_crow.convert_space(source)
    target = eso_crow.convert_space(target)

    result = eso_crow.dijkstra(source, target)

    if isinstance(result, list):
        return render_template('dijkstra.html', pairs_list=result, source=source, target=target)

    else:
        return render_template('dijkstra.html', error_message=result)


@ app.route('/random_route')
def random_route():

    nodes = eso_crow.locations

    url1 = choice(nodes)
    url2 = choice(nodes)

    while url1 == url2:
        url2 = choice(nodes)

    return redirect(f'/{url1}/{url2}')
