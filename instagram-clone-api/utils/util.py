from fastapi import UploadFile, File
import string
import random
import shutil

from database.db import Base, engine, SessionLocal
from models import user_model, post_model


def add_tables():
    print("Creating database...")
    return Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def upload_file(image: UploadFile = File(...)):
    letters = string.ascii_letters
    rand_str = "".join(random.choice(letters) for i in range(6))
    new = f"_{rand_str}."
    filename = new.join(image.filename.rsplit(".", 1))
    path = f"images/{filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": path}
