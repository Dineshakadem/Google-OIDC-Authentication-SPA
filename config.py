import os

class Config:
    SECRET_KEY = "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"
    OIDC_CLIENT_SECRETS = 'client_secret.json'  
    OIDC_RESOURCE_SERVER_ONLY = False
    OIDC_SCOPES = ['openid', 'email', 'profile']
    OIDC_REDIRECT_URI = 'http://127.0.0.1:5000/authorize'
