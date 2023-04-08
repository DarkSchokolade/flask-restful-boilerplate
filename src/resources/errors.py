from werkzeug.exceptions import HTTPException


class InternalServerError(HTTPException):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong.",
        "status": 500
    }
}