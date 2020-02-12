import os
import json
import boto3
from botocore.exceptions import ClientError


# Esta função busca o valor de um secret armazenado no AWS Secrets Manager a partir de um secret name
# ==================================================================
def get_secret(secret_name):
    print('[get_secret][{}]: inicio'.format(secret_name))
    my_session = boto3.session.Session()
    region_name = my_session.region_name

    try:
        client = my_session.client(service_name='secretsmanager', region_name=region_name)
        response = client.get_secret_value(SecretId=os.getenv(secret_name))
        print('[get_secret][{}]: fim'.format(secret_name))
        return json.loads(response['SecretString'])
    except ClientError as e:
        print(e)