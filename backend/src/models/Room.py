from sqlalchemy import (
    Column,
    CHAR,
    Boolean
)

from backend.src.db_access.globals import Base


class Room(Base):
    __tablename__ = "Room"

    room_id = Column(CHAR(36), primary_key=True)
    disappearing = Column(Boolean)
