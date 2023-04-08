from .my_resource import MyResource, DivideBy


def initialize_routes(api):
    api.add_resource(MyResource, "/")
    api.add_resource(DivideBy, "/<int:divisor>")
