from fastapi import FastAPI
from services.db_service import _add_tables

app = FastAPI()


_add_tables()
