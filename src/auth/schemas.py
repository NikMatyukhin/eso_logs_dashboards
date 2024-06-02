from pydantic import BaseModel


class AuthRequestBody(BaseModel):
    grant_type: str


class AuthResponseBody(BaseModel):
    token_type: str
    expires_in: int
    access_token: str
