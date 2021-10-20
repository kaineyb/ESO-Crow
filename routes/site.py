from app import app
from flask import render_template
from esocrow.main import locations, list_for_zones


@ app.route('/')
def index():
    """
    Returns the template for index.html and passes it the locations list.
    (locations list is Used for Javascript Autocomplete)
    """
    return render_template('index.html', locations=locations)


@ app.errorhandler(404)
def page_not_found():
    """ Returns the template for page_not_found.html  """
    return render_template('errors/page_not_found.html'), 404


@ app.route('/updates')
def updates():
    """ Returns the template for updates.html"""
    return render_template('site/updates.html')


@ app.route('/tip')
def tip():
    """ Returns the template for tip.html"""
    return render_template('site/tip.html')


@ app.route('/faq')
def faq():
    """ Returns the template for faq.html """
    return render_template('site/faq.html')


@ app.route('/locations')
def get_locations():
    """ Returns the template for locations.html and passes it the locations list """
    return render_template('supplementary/locations.html', locations=locations)


@ app.route('/zones')
def get_zones():
    """ Returns the template for zones.html and passes it the zones list """
    return render_template('supplementary/zones.html', zone_info=list_for_zones)
