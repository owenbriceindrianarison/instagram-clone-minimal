from database.db import Base, engine, SessionLocal

from models import user_model, post_model


def _add_tables():
    print("Creating database...")
    return Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
