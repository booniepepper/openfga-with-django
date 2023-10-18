# from django.shortcuts import render
from django.http import HttpResponse

import asyncio
import os
import openfga_sdk
from openfga_sdk.client import OpenFgaClient
from openfga_sdk.credentials import Credentials, CredentialConfiguration

configuration = openfga_sdk.ClientConfiguration(
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


def read_authorization_models():
    async def call():
        async with OpenFgaClient(configuration) as fga_client:
            response = await fga_client.read_authorization_models()
        return response
    return asyncio.run(call())


def index(request):
    auth_models = read_authorization_models()

    return HttpResponse(auth_models)
