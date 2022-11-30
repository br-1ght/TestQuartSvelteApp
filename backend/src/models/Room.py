from sqlalchemy import (
    Column,
    CHAR,
    Boolean
)

from .db import Base


class Room(Base):
    __tablename__ = "Room"

    room_id = Column(CHAR(36), primary_key=True)
    disappearing = Column(Boolean)


