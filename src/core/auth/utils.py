import requests
from requests.auth import HTTPBasicAuth

from src.settings import AuthSettings

from .schemas import AuthRequestBody, AuthResponseBody


def authenticate(settings: AuthSettings) -> AuthResponseBody:
    """
    Authenticate application by client credentials flow.

    https://www.archon.gg/eso/articles/help/api-documentation
    """

    data = AuthRequestBody(grant_type=settings.grant_type)
    auth = HTTPBasicAuth(
        username=settings.client_id,
        password=settings.client_secret,
    )

    response = requests.post(
        url=settings.oauth_token_url,
        data=data.model_dump(),
        auth=auth,
    )

    # TODO: results (ok/err) maybe better?
    if response.status_code != requests.codes.ok:
        raise requests.HTTPError

    return AuthResponseBody.model_validate(response.json())


def get_token(settings: AuthSettings) -> str:
    auth_response = authenticate(settings)
    return auth_response.access_token
