
from os import environ


class BaseMeta:

    TOKEN = environ.get('M2TOKEN')

    PREFIX = '2'
