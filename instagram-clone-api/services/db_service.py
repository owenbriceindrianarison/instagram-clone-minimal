from database.db import Base, engine, SessionLocal


def _add_tables():
    print("Creating database...")
    return Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
