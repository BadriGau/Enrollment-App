import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'[\xf6\xf5\x1b\xc9M\x02\x0eN\x1e#.\xc5\xa7\nk'
    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }
    