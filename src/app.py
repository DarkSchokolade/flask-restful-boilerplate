import os
from initialise import app
from flask_restful import Api
from resources.errors import errors
from resources.routes import initialize_routes


if __name__ == "__main__":
    api = Api(app, errors=errors)
    initialize_routes(api)

    PORT = os.environ.get("PORT")
    HOST = os.environ.get("HOST")
    app.run(port=PORT, host=HOST, debug=True)
