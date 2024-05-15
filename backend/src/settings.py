import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# -*- coding: utf-8 -*-
DATABASE_LOGIN = 'postgres'
DATABASE_PASS = 'postgres'
# flask core settings
DEBUG = False
TESTING = False
SECRET_KEY = "1234566778"
PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 30
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=3)

# flask wtf settings
WTF_CSRF_ENABLED = True

# flask mail settings
#MAIL_DEFAULT_SENDER =os.environ.get('MAIL_DEFAULT_SENDER')
SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_LOGIN}:{DATABASE_PASS}@192.168.56.105/app_presente'