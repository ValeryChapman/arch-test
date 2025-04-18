from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED

from internal.common.exceptions.authorization import UnauthorizedError
from internal.common.exceptions.fakestoreapi import RequestFailed
from internal.common.responses.failed import DefaultErrorResponseSchema


def add_exception_handlers(app: FastAPI):
    @app.exception_handler(RequestFailed)
    async def handle_fakestoreapi_error(_, exc):
        return JSONResponse(
            content=DefaultErrorResponseSchema(
                status=False, message=exc.message
            ).model_dump(),
            status_code=HTTP_400_BAD_REQUEST,
        )

    @app.exception_handler(UnauthorizedError)
    async def handle_user_unauthorized_error(_, exc):
        return JSONResponse(
            content=DefaultErrorResponseSchema(message=exc.message).model_dump(),
            status_code=HTTP_401_UNAUTHORIZED,
        )
