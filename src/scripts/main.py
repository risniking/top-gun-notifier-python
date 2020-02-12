import json
from core_auth import get_token
from slacker import create_slack_client, send_message
from core_application import get_application_id_by_cpf


def main_handler(event, context):
    cpf = event['cpf']
    user = event['user']
    requester = event['requester']
    alteration = event['alteration']
    channel = event['channel']

    token = get_token()

    application_id = get_application_id_by_cpf(cpf, token)

    lead_mdo_url = 'https://mdo.creditas.com.br/auto-refi/{}/fichas-parceiros'.format(application_id)

    message_template = '''
        Oi, <@{}>! Tem uma solicitação do {} para aletrar {}. O cliente é o {}
    '''

    slack_client = create_slack_client()

    send_message(
        slack_client,
        channel,
        message_template.format(user, requester, alteration, lead_mdo_url)
    )

    return
