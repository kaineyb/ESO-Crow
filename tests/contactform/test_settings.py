

from contact_form.settings import init_mail


def test_settings():
    """ Checks the link isn't broken. """

    assert init_mail
