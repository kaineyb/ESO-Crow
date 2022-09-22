import os


def get_environ():

    if os.environ.get("LOCAL"):
        print("  ", "*" * 20)
        print("   Local Environment")
        print("  ", "*" * 20)

        print("   Keys Loaded:")

        for key in keys:
            print("   ", key)

    elif os.environ.get("PRODUCTION"):
        print("  ", "*" * 20)
        print("   Production Environment")
        print("  ", "*" * 20)

        for key in keys:
            print("   ", key)

    else:
        print("  ", "*" * 20)
        print("Environment Unknown")
        print("  ", "*" * 20)


PUBLIC = os.environ.get("PUBLIC_KEY")
PRIVATE = os.environ.get("PRIVATE_KEY")
EMAIL = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASS = os.environ.get("EMAIL_PASSWORD")
SECRET_KEY = os.environ.get("SECRET_KEY")

keys = [PUBLIC, PRIVATE, EMAIL, EMAIL_PASS, SECRET_KEY]

get_environ()
