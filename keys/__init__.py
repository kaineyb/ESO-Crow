import os


def get_environ():

    if os.environ.get("ENVIRON_TYPE") == "LOCAL":
        load_environment("Local Environment")

    elif os.environ.get("ENVIRON_TYPE") == "PROD":
        load_environment("Production Environment")

    else:
        load_environment("Environment Unknown, ENVIRON_TYPE not set")


def load_environment(environment_detail):
    divider()
    print(f"\t{environment_detail}")
    divider()
    print("\tKeys Loaded:")
    divider()
    for key, value in keys.items():
        print(f"\t{key}: {value}")


def divider():
    print(f"\t{'*' * 20}")


keys = {
    "PUBLIC": os.environ.get("PUBLIC_KEY"),
    "PRIVATE": os.environ.get("PRIVATE_KEY"),
    "EMAIL": os.environ.get("EMAIL_ADDRESS"),
    "EMAIL_PASS": os.environ.get("EMAIL_PASSWORD"),
    "SECRET_KEY": os.environ.get("SECRET_KEY"),
    "ENVIRON_TYPE": os.environ.get("ENVIRON_TYPE"),
}

get_environ()
