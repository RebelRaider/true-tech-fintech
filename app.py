import sys

from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from errors.handlers import init_exception_handlers
from routing.v1.action_template import router as action_template_router
from routing.v1.active_action import router as active_action_router
from routing.v1.ml import router as ml_router

from configs.Environment import get_environment_variables


app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

env = get_environment_variables()

init_exception_handlers(app)

if not env.DEBUG:
    logger.remove()
    logger.add(sys.stdout, level="INFO")

app.include_router(action_template_router)
app.include_router(active_action_router)
app.include_router(ml_router)
