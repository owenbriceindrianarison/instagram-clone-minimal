from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from utils.util import add_tables
from routers import auth_router, post_router, comment_router

app = FastAPI()

app.include_router(auth_router.router)
app.include_router(post_router.router)
app.include_router(comment_router.router)

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_tables()

app.mount("/images", StaticFiles(directory="images"), name="images")
