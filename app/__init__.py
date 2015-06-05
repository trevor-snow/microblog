import os
from flask.ext.login import Login Manager
from flask.ext.openid import OpenID
from config import basedir


lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
