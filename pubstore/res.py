from flask import request, Response

from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from .library import Key, db_session as db
from .parser import key_parser


class Keys(Resource):
    def __init__(self):
        Resource.__init__(self)
        self.KeyModel = Key
        self.parser = key_parser

    def get(self, mimetype="json"):
        if mimetype == "json":
            return {
                'keys': {
                    k.id: {
                        "type": k.key_type,
                        "value": k.key_value,
                        "comment": k.key_comment,
                        "creation_time": str(k.creation_time)
                    } for k in self.KeyModel.query.all()
                }
            }
        elif mimetype == "text":
            response = Response(
                response='\n'.join(
                    [k.recombined() for k in self.KeyModel.query.all()]
                ),
                status=200,
                mimetype='text/plain'
            )
            return response

    def post(self):
        args = self.parser.parse_args()
        keys = args['pubkey']
        results = []
        if isinstance(keys, (list,)):
            for key in keys:
                results.append(self.try_commit_key(key))
        else:
            results = self.try_commit_key(keys)
        return results

    def try_commit_key(self, key):
        k = self.KeyModel(
            value=key)
        try:
            db.add(k)
            db.commit()
            return {
                    "type": k.key_type,
                    "value": k.key_value,
                    "comment": k.key_comment,
                "creation_time": str(k.creation_time)}

        except IntegrityError as ie:
            db.rollback()
            return {'key': k.recombined(), 'error': ie.args}
