import json
import os
import requests

def get_appconfig_data(application_name, environment_name, configuration_name):
    url = f'http://localhost:2772/applications/{application_name}/environments/{environment_name}/configurations/{configuration_name}'
    print(f"Making request to: {url}")
    config = requests.get(url).json()
    return config

def lambda_handler(event, context):
    application_name = os.getenv("APPCONFIG_APPLICATION")
    environment_name = os.getenv("APPCONFIG_ENVIRONMENT")
    configuration_name = os.getenv("APPCONFIG_CONFIGURATION")
    print(f"{application_name}\n{environment_name}\n{configuration_name}")
    return {
        "statusCode": 200,
        "body": json.dumps(get_appconfig_data(application_name, environment_name, configuration_name))
    }
