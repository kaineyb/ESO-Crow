from keys import keys


def test_secrets():
    assert keys["ENVIRON_TYPE"] != None
    assert keys["PUBLIC"] != None
    assert keys["PRIVATE"] != None
    assert keys["EMAIL"] != None
    assert keys["EMAIL_PASS"] != None
    assert keys["SECRET_KEY"] != None
