import os
from slack import WebClient


def create_slack_client():
    slack_client = WebClient(token=os.getenv('SLACK_TOKEN'))

    return slack_client

def send_message(client, channel, message):
    client.chat_postMessage(
        channel=channel,
        text=message
    )
