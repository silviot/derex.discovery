# flake8: noqa
# type: ignore

from .derex import *

FEATURES["ENABLE_OAUTH2_PROVIDER"] = True
OAUTH_OIDC_ISSUER = "http://lms.localhost:4700/oauth2"

JWT_AUTH["JWT_ISSUER"] = JWT_ISSUER
JWT_AUTH["JWT_AUDIENCE"] = JWT_AUDIENCE
JWT_AUTH["JWT_SECRET_KEY"] = JWT_SECRET_KEY
