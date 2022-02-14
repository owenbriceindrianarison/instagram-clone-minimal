from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from utils.util import add_tables
from routers import auth_router, post_router, comment_router

app = FastAPI()

app.include_router(auth_router.router)
app.include_router(post_router.router)
app.include_router(comment_router.router)

add_tables()

app.mount("/images", StaticFiles(directory="images"), name="images")
