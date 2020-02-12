import os
import json
from requests import request


# =========== Globals ===========

# variáveis de request
password_token =            os.getenv('PASSWORD_TOKEN')
user_token =                os.getenv('USER_TOKEN')
url_token =                 os.getenv('URL_TOKEN')
password_token_staging =    os.getenv('PASSWORD_TOKEN_STAGING')
user_token_staging =        os.getenv('USER_TOKEN_STAGING')
url_token_staging =         os.getenv('URL_TOKEN_STAGING')

# =========== Methods ===========

# Request de token de acesso ao MDO
# ================================================================================================
def get_token(config='production'):
    print('[get_token]: início')
    token = False

    # credenciais
    header = {
        "Content-Type": "application/json",
        "Accept": "application/vnd.api+json",
        "Accept-Version": "v1"
    }

    if config == 'production':
        url = url_token
        body = {
            "grant_type": "password",
            "username": user_token,
            "password": password_token
        }

    else:
        url = url_token_staging
        body = {
            "grant_type": "password",
            "username": user_token_staging,
            "password": password_token_staging
        }

    try:
        body = json.dumps(body)
        request_response = request("POST", url, data=body, headers=header)

        # endpoint retorna 201 para sucesso
        if request_response.status_code == 201 or request_response.status_code == 200:
            response_json = request_response.json()
            token = response_json['access_token']

    except Exception as exc:
        print('[get_token]: Exception {}'.format(exc))

    print('[get_token]: fim')
    return token
