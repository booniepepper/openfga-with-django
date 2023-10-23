# from django.shortcuts import render
from django.http import HttpResponse

import os
import openfga_sdk_sync
from openfga_sdk_sync.client import OpenFgaClient
from openfga_sdk_sync.credentials import Credentials, CredentialConfiguration

configuration = openfga_sdk_sync.ClientConfiguration(
    api_host='api.us1.fga.dev',
    store_id='01H8M76TB3P7EWC6T298WTJX2D',
    credentials=Credentials(
        method='client_credentials',
        configuration=CredentialConfiguration(
            api_issuer='fga.us.auth0.com',
            api_audience='https://api.us1.fga.dev/',
            client_id='P99BJ2XKlB1N8NdIPzN5Ew8mBegEz0FJ',
            client_secret=os.getenv('OPENFGA_CLIENT_SECRET')
        )
    )
)

fga_client = OpenFgaClient(configuration)


def auth_models(request):
    models = fga_client.read_authorization_models()
    return HttpResponse(models)
