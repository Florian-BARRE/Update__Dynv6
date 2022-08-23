import json
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
SECRET_FILE_PATH = 'secrets.json'
SECRET_CONFIG_STORE = {}

try:
    with open(SECRET_FILE_PATH) as config:
        SECRET_CONFIG_STORE = json.load(config)
except FileNotFoundError:
    try:
        with open(os.path.join(BASE_DIR, 'secrets.json')) as config:
            SECRET_CONFIG_STORE = json.load(config)
    except Exception:
        raise


class BaseConfig(object):
    APPLICATION_NAME = 'Update_Dynv6'
    BASE_DIR = BASE_DIR


class ProductionConfig(BaseConfig):
    ENV = "production"
    DEBUG = 1
    PRIORITY_DEBUG_LEVEL = 100
    GET_IP_URL = 'https://duckduckgo.com/?q=ip&format=json'
    REFRESH_DELAY = 120
    TOKEN = SECRET_CONFIG_STORE["token"]
    ZONE = SECRET_CONFIG_STORE["zone"]
    GLOBAL = dict()


class LocalConfig(BaseConfig):
    pass


class ConfigurationException(Exception):
    pass


class Configuration(dict):
    def __init__(self, *args, **kwargs):
        if not os.environ.get('ENV'):
            raise ConfigurationException(
                "Please set 'ENV' environment variable"
            )

        super(Configuration, self).__init__(*args, **kwargs)

        self["ENV"] = os.environ['ENV']
        self.__dict__ = self

    def from_object(self, obj):
        for attr in dir(obj):

            if not attr.isupper():
                continue

            self[attr] = getattr(obj, attr)

        self.__dict__ = self


APP_CONFIG = Configuration()

if APP_CONFIG.get('ENV') == 'production':
    APP_CONFIG.from_object(ProductionConfig)
elif APP_CONFIG.get('ENV') == 'local':
    APP_CONFIG.from_object(LocalConfig)
else:
    APP_CONFIG.from_object(ConfigurationException)
