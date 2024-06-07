import requests
import requests.auth
from gql import Client
from gql.transport.requests import RequestsHTTPTransport

from src.settings import ApplicationSettings, AuthSettings, get_settings

from .schemas import AuthRequestBody, AuthResponseBody


def authenticate(settings: AuthSettings) -> AuthResponseBody:
    """
    Authenticate application by client credentials flow.

    https://www.archon.gg/eso/articles/help/api-documentation
    """

    data = AuthRequestBody(grant_type=settings.grant_type)
    auth = requests.auth.HTTPBasicAuth(
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


class AuthenticatedFetcher:
    """
    Base class for all fetchers with authenticated GraphQL client.
    """

    _client: Client | None = None

    @property
    def client(self) -> Client:
        if self._client is not None:
            return self._client

        app_settings = get_settings(ApplicationSettings)
        auth_settings = get_settings(AuthSettings)
        auth_response = authenticate(auth_settings)

        transport = RequestsHTTPTransport(
            url=app_settings.client_endpoint_url,
            headers={
                auth_settings.token_header: auth_settings.token_type
                + " "
                + auth_response.access_token
            },
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)

        self._client = client
        return client
