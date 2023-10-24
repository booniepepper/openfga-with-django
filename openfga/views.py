# from django.shortcuts import render
from django.http import HttpResponse

import os
import openfga_sdk
import openfga_sdk.credentials
import openfga_sdk.sync
import openfga_sdk.sync.credentials


# Async (Existing)

configuration = openfga_sdk.ClientConfiguration(
    api_host='api.us1.fga.dev',
    store_id='01H8M76TB3P7EWC6T298WTJX2D',
    credentials=openfga_sdk.credentials.Credentials(
        method='client_credentials',
        configuration=openfga_sdk.credentials.CredentialConfiguration(
            api_issuer='fga.us.auth0.com',
            api_audience='https://api.us1.fga.dev/',
            client_id='P99BJ2XKlB1N8NdIPzN5Ew8mBegEz0FJ',
            client_secret=os.getenv('OPENFGA_CLIENT_SECRET')
        )
    )
)

fga_client = openfga_sdk.OpenFgaClient(configuration)


async def auth_models(request):
    models = await fga_client.read_authorization_models()
    return HttpResponse(models)


# Synchronous (New, all imports subject to change)

configuration_sync = openfga_sdk.ClientConfiguration(
    api_host='api.us1.fga.dev',
    store_id='01H8M76TB3P7EWC6T298WTJX2D',
    credentials=openfga_sdk.sync.credentials.Credentials(
        method='client_credentials',
        configuration=openfga_sdk.sync.credentials.CredentialConfiguration(
            api_issuer='fga.us.auth0.com',
            api_audience='https://api.us1.fga.dev/',
            client_id='P99BJ2XKlB1N8NdIPzN5Ew8mBegEz0FJ',
            client_secret=os.getenv('OPENFGA_CLIENT_SECRET')
        )
    )
)

fga_client_sync = openfga_sdk.sync.OpenFgaClient(configuration_sync)


def auth_models_sync(request):
    models = fga_client_sync.read_authorization_models()
    return HttpResponse(models)
