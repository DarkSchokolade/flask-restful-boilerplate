from flask_restful import Resource
from .errors import InternalServerError


class MyResource(Resource):
    def get(self):
        return "Hello There!!!"


class DivideBy(Resource):
    def get(self, divisor):
        try:
            result = 100 / divisor
            return result
        except Exception as err:
            print(err)
            raise InternalServerError
