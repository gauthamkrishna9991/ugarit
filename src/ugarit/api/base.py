"""
Base Application
"""
from sqlalchemy.orm import Session

from ugarit import schemas
from ugarit.config import ServerConfig
from ugarit.database import SessionLocal, engine

if ServerConfig.debug:
    print("Database in Debug Mode")
    schemas.base.Base.metadata.drop_all(bind=engine)

schemas.base.Base.metadata.create_all(bind=engine)


# Dependency
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
