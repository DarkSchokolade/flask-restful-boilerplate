from .my_resource import MyResource, DivideBy
from .user_handler import UserHandler


def initialize_routes(api):
    api.add_resource(MyResource, "/")
    api.add_resource(DivideBy, "/<int:divisor>")
    api.add_resource(UserHandler, "/user")
