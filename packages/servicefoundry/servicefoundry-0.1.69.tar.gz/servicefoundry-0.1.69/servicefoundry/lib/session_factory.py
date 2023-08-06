import json
import os

from servicefoundry.lib.clients.auth_service_client import AuthServiceClient
from servicefoundry.lib.const import DEFAULT_TENANT_ID, SESSION_FILE
from servicefoundry.lib.exceptions import BadRequestException
from servicefoundry.lib.model.session import ServiceFoundrySession


def get_session(session_file=SESSION_FILE):
    if os.getenv("SERVICE_FOUNDRY_API_KEY"):
        auth_client = AuthServiceClient()
        return auth_client.login_with_api_token(
            DEFAULT_TENANT_ID, os.getenv("SERVICE_FOUNDRY_API_KEY")
        )

    if os.path.isfile(session_file):
        with open(session_file, "r") as file:
            data = json.load(file)
            return ServiceFoundrySession(
                **data, refresher=AuthServiceClient().refresh_token
            )
    else:
        raise BadRequestException(403, f"Please login before running this command.")


def logout_session(session_file=SESSION_FILE):
    # TODO: Implement logout if using api key
    if os.path.isfile(session_file):
        with open(session_file, "r") as file:
            data = json.load(file)
            _ = ServiceFoundrySession(
                **data, refresher=AuthServiceClient().refresh_token
            )
        os.remove(session_file)
    else:
        raise BadRequestException(403, f"Please login before running this command.")
