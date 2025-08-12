from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider, setup_dishka
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from test_app.application.provider.gateways_provider import GatewaysProvider


def setup_containers(app: FastAPI) -> None:
    container = make_async_container(GatewaysProvider())

    setup_dishka(container, app)


def create_app() -> FastAPI:
    app = FastAPI(default_response_class=ORJSONResponse)

    setup_containers(app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173", "http://127.0.0.0:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )

    return app


app = create_app()
