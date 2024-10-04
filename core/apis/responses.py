from flask import Response, jsonify, make_response


class APIResponse(Response):
    @classmethod
    def respond(cls, data):
        return make_response(jsonify(data=data))

    # @classmethod
    # def respond_with_error(cls, error="FyleError", status_code=400, message=None):
    #     """Error response with a message and optional details"""
    #     error_response = {
    #         'error': message
    #     }
    #     return make_response(jsonify(error=error,message=message), status_code)
