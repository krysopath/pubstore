from sqlalchemy import Column, Integer, Sequence, String, TIMESTAMP
from sqlalchemy.sql import func
from ..database import Base
from .skeleton import Skeleton

__all__ = ['Key']


class Key(Base, Skeleton):
    modelname = "Key"
    __tablename__ = "keys"
    id = Column(
        Integer,
        Sequence('key_id_seq'),
        primary_key=True
    )
    key_type = Column(
        String,
        nullable=False,

    )
    key_value = Column(
        String,
        nullable=False,
        unique=True
    )
    key_comment = Column(
        String,
        nullable=False,
    )
    creation_time = Column(
        TIMESTAMP,
        server_default=func.now(),
        nullable=False
    )
    export = [
        'id',
        'key_type',
        'key_value',
        'key_comment',
        'creation_time'
    ]

    def __init__(self, value=None, *args, **kwargs):
        self.key_type, self.key_value, self.key_comment = value.split(' ')

    def __repr__(self):
        return "<Key(value=%r)>" \
               % self.value

    def recombined(self):
        return "%s %s %s" % (self.key_type, self.key_value, self.key_comment)
