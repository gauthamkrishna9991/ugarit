from ugarit import schemas
from ugarit.database import SessionLocal, engine

schemas.base.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
