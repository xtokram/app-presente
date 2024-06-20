import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# -*- coding: utf-8 -*-
DATABASE_LOGIN = os.environ.get('DATABASE_LOGIN')
DATABASE_PASS = os.environ.get('DATABASE_SENHA')
DATABASE_IP = os.environ.get('DATABASE_IP')

# flask core settings
DEBUG = False
TESTING = False
SECRET_KEY = os.environ.get('SECRET_KEY')
PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 30
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=3)
OIDC_CLIENT_SECRETS = 'client_secrets_prod.json'
OIDC_OPENID_REALM = 'app-presente'
OIDC_ID_TOKEN_COOKIE_SECURE = False
OIDC_SCOPES=['openid']
HANDLER = "StreamHandler"
# flask wtf settings
WTF_CSRF_ENABLED = True

# flask mail settings

#MAIL_DEFAULT_SENDER =os.environ.get('MAIL_DEFAULT_SENDER')
SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_LOGIN}:{DATABASE_PASS}@{DATABASE_IP}/app_presente'

# Redis
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')