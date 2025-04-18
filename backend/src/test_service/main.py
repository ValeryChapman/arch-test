from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from internal.controllers.http.extensions import add_exception_handlers
from internal.controllers.http.router import router as http_router

app = FastAPI()

app.add_middleware(
    middleware_class=CORSMiddleware,  # noqa
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=http_router)
add_exception_handlers(app=app)
