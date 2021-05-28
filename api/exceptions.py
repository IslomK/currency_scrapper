from flask import jsonify

from api import app


class BaseError(Exception):
    status_code = None

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['status'] = 'error'
        rv['message'] = self.message
        return rv


class InternalServerError(BaseError):
    status_code = 500


class BadRequest(BaseError):
    status_code = 400


class NotFoundError(BaseError):
    status_code = 404


@app.errorhandler(BadRequest)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(InternalServerError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

