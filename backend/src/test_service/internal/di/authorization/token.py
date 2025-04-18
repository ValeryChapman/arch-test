from fastapi import Header

from core.settings.settings import settings
from internal.common.exceptions.authorization import UnauthorizedError

API_KEY_NAME = "X-API-Key"


async def api_key_authorization(x_api_key: str = Header(..., alias=API_KEY_NAME)):
    if x_api_key != settings.authorization.api_key:
        raise UnauthorizedError("Invalid or missing API key")
