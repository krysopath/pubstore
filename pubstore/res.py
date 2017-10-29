from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from .library import Key, db_session as db
from .parser import key_parser


class Keys(Resource):
    def __init__(self, *args, **kwargs):
        Resource.__init__(self, *args, **kwargs)
        self.Model = Key
        self.parser = key_parser

    def get(self):
        return {
            'keys': {
                k.id: {
                    "type": k.key_type,
                    "value": k.key_value,
                    "comment": k.key_comment,
                    "creation_time": str(k.creation_time)
                } for k in self.Model.query.all()
            }
        }

    def post(self):
        args = self.parser.parse_args()
        k = self.Model(
            value=args['pubkey']
        )

        try:
            db.add(k)
            db.commit()
            return {
                'key': {
                    "type": k.key_type,
                    "value": k.key_value,
                    "comment": k.key_comment,
                    "creation_time": str(k.creation_time)
                },
            }

        except IntegrityError as ie:
            db.rollback()
            return {'key': False, 'reason': ie.args}
