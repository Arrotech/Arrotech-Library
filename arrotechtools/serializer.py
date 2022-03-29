from flask import make_response, jsonify


class Serializer:
    """Serialize data output.
    """

    def __init__(self):
        """Class constructor.
        """

    @classmethod
    def serialize(cls, response: list, message: str, status_code: int):
        """_summary_

        Args:
            response (list): _description_
            message (str): _description_
            status_code (int): _description_

        Returns:
            _type_: _description_
        """
        if status_code in (400, 401, 403, 404, 405, 500):
            return make_response(jsonify({
                "status": status_code,
                "message": message,
                "error": response
            }), status_code)
        return make_response(jsonify({
            "status": status_code,
            "message": message,
            "data": response
        }), status_code)

    @classmethod
    def on_success(cls, message: str, status_code: int):
        """_summary_

        Args:
            message (str): _description_
            status_code (int): _description_

        Returns:
            _type_: _description_
        """
        return make_response(jsonify({
            "status": status_code,
            "message": message,
        }), status_code)


class ErrorHandler:
    """Class error handler.
    """

    def __init__(self):
        """Class constructor.
        """

    @classmethod
    def raise_error(cls, message: str, status_code: int):
        """_summary_

        Args:
            message (str): _description_
            status_code (int): _description_

        Returns:
            _type_: _description_
        """
        return make_response(jsonify({
            "status": status_code,
            "message": message,
        }), status_code)

    @classmethod
    def bad_request(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        return make_response(jsonify({
            "status": "400",
            "message": "bad request"
        }), 400)

    @classmethod
    def page_not_found(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        return make_response(jsonify({
            "status": "404",
            "message": "resource not found"
        }), 404)

    @classmethod
    def method_not_allowed(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        return make_response(jsonify({
            "status": "405",
            "message": "method not allowed"
        }), 405)

    @classmethod
    def internal_server_error(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        return make_response(jsonify({
            "status": "500",
            "message": "internal server error"
        }), 500)
