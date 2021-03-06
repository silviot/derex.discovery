# flake8: noqa
# type: ignore

from .derex import *

FEATURES["ENABLE_OAUTH2_PROVIDER"] = True
OAUTH_OIDC_ISSUER = "http://lms.localhost:4700/oauth2"

JWT_AUTH["JWT_ISSUER"] = JWT_ISSUER
JWT_AUTH["JWT_AUDIENCE"] = JWT_AUDIENCE
JWT_AUTH["JWT_SECRET_KEY"] = JWT_SECRET_KEY
JWT_AUTH["JWT_PRIVATE_SIGNING_JWK"] = JWT_PRIVATE_SIGNING_JWK
JWT_AUTH["JWT_PUBLIC_SIGNING_JWK_SET"] = JWT_PUBLIC_SIGNING_JWK_SET
JWT_AUTH["JWT_SIGNING_ALGORITHM"] = JWT_SIGNING_ALGORITHM

ECOMMERCE_PUBLIC_URL_ROOT = "http://ecommerce.localhost:4900"
ECOMMERCE_API_URL = "http://ecommerce.localhost:4900/api/v2"

COURSE_CATALOG_API_URL = "http://discovery.localhost:4910"
