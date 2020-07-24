# secret_key was set with os.urandom(20)
class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:pewdiepie@localhost/recipe'
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = "\xf9\xe5u\xd3\xee\x00\x0b\x08\xea\xa5X\x8a'\xdb\xa8\x9b6\xe6\xd4\xc8\x97\x05\x9b\xe1"
