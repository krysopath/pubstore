from flask_restful import reqparse

key_parser = reqparse.RequestParser()
key_parser.add_argument('pubkey', type=str)
