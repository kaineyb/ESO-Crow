import keys


def test_secrets():
    assert keys.PUBLIC != None
    assert keys.PRIVATE != None
    assert keys.EMAIL != None
    assert keys.EMAIL_PASS != None
    assert keys.SECRET_KEY != None
