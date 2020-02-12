import os
import json
from requests import request


# =========== Methods ===========
# Busca application id usando cpf
def get_application_id_by_cpf(cpf, token):
    query_cpf_endpoint = 'https://core.creditas.com.br/crm/customers?filter%5Bquery%5D={}'.format(cpf)

    headers = {
        'Accept': 'application/vnd.api+json',
        'Authorization': 'Bearer {}'.format(token),
        'Accept-Version': 'v1'
    }

    method = 'GET'

    lead_list_response = request(method=method, url=query_cpf_endpoint, headers=headers)
    lead_list = lead_list_response.json()

    lead_id = lead_list['data']['relationships']['active-auto-refi-lead']['data']['id']

    query_active_application_endpoint = 'https://core.creditas.com.br/crm/auto-refi/leads/{}/application'.format(lead_id)

    application_response = request(method=method, url=query_active_application_endpoint, headers=headers)
    application = application_response.json()

    application_id = application['data']['id']

    return application_id

# Retorna application data
# ==================================================================
def get_application_data(data, token):
    print('[get_application_data]: inicio')
    method = 'GET'

    url_app = 'https://core.creditas.com.br/loan/auto-refi/bkf/applications/' + data['id']

    headers = {
      'Accept': 'application/vnd.api+json',
      'Accept-Version': 'v1',
      'Authorization': token,
      'Cache-Control': 'no-cache',
      'json': 'true',
    }

    try:
        response = request(method, url_app, headers = headers, timeout = 30)
        response = response.json()

        return response
    except Exception as exc:
        print('[get_application_data]: Exceção {}'.format(exc))

def isIQ(data, token):
    applicationData = get_application_data(data, token)

    return applicationData['data']['attributes']['iq']
