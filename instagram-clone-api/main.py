from fastapi import FastAPI
from utils.db_util import _add_tables
from routers import auth_router

app = FastAPI()

app.include_router(auth_router.router)

_add_tables()
