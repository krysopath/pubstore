from flask import request
from flask_restful import Resource
from .library import Key, db_session as db


class Keys(Resource):

    def __init__(self, *args, **kwargs):
        Resource.__init__(self, *args, **kwargs)
        self.model = Key

    def get(self):
        return {
            'known_keys': [
                k.value for k
                in self.model.query.all()
            ]
        }

    def post(self):
        k = self.model(
            value=request.form['pubkey']
        )
        try:
            db.add(k)
            db.commit()
            return {'key': k.value}

        except Exception as e:
            db.rollback()
            return {'key': False}





