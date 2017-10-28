from sqlalchemy import Column, Integer, Sequence, String, ForeignKey, Boolean
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
    value = Column(
        String,
        nullable=False,
        unique=True
    )
    export = [
        'id',
        'value',
    ]

    def __init__(self, value=None, *args, **kwargs):
        self.value = value

    def __repr__(self):
        return "<Key(value=%r)>" \
               % self.value
