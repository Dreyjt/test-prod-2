import boto3
import json


def get_secrets():
    client = boto3.client("secretsmanager", region_name="us-east-1")

    response = client.get_secret_value(
        SecretId="internal-app-secrets"
    )

    secret = json.loads(response["SecretString"])
    return secret
