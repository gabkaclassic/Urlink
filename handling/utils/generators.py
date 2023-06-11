import string
from random import choice


def random_string(length=6):
    return ''.join(choice(CHARACTERS) for i in range(length))


CHARACTERS = string.ascii_letters + string.digits + string.punctuation
