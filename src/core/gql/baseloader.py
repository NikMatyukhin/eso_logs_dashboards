from gql import Client
from gql.transport.requests import RequestsHTTPTransport

from core.auth import get_token
from settings import ApplicationSettings, AuthSettings, get_settings


class GraphQLBaseLoader:
    _client: Client | None = None

    @property
    def client(self) -> Client:
        if self._client is not None:
            return self._client

        app_settings = get_settings(ApplicationSettings)
        auth_settings = get_settings(AuthSettings)
        token = get_token(auth_settings)

        transport = RequestsHTTPTransport(
            url=app_settings.client_endpoint_url,
            headers={
                auth_settings.token_header: f"{auth_settings.token_type} {token}",
            },
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)

        self._client = client
        return client
