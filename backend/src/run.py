from application import create_app
from waitress import serve

from utils import oidc


app = create_app('settings.py')
oidc.init_app(app)


serve(app, host="0.0.0.0", port=5000)