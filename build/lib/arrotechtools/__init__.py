import json
import re
import os
from functools import wraps
from flask_jwt_extended import get_jwt_identity


class Validators:
    """Class with validation methods."""

    def __init__(self, variable=None):
        self.variable = variable

    def email(self):
        """Check if the format of the email is valid."""
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$)",
                    self.variable):
            return True
        return False

    def password(self):
        """Check if that the password is eight long character string with atleast one lowercase character, one uppercase character, one number, and one special character."""
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", self.variable):
            return True
        return False

    def phone(self):
        """Check if that the phone number satisfies kenyan format."""
        if re.match(r"^(?:254|\+254|0)?(7(?:(?:[129][0-9])|(?:0[0-8])|(4[0-1]))[0-9]{6})$", self.variable):
            return True
        return False

    def safaricom(self):
        """Check if that the phone number satisfies safaricom format."""
        if re.match(r"^(?:254|\+254|0)?(7(?:(?:[129][0–9])|(?:0[0–8])|(4[0–1]))[0–9]{6})$", self.variable):
            return True
        return False

    def airtel(self):
        """Check if that the phone number satisfies airtel format."""
        if re.match(r"^(?:254|\+254|0)?(7(?:(?:[3][0-9])|(?:5[0-6])|(8[0-9]))[0-9]{6})$", self.variable):
            return True
        return False

    def orange(self):
        """Check if that the phone number satisfies orange format."""
        if re.match(r"^(?:254|\+254|0)?(77[0-6][0-9]{6})$", self.variable):
            return True
        return False

    def equitel(self):
        """Check if that the phone number satisfies equitel format."""
        if re.match(r"^(?:254|\+254|0)?(76[34][0-9]{6})$", self.variable):
            return True
        return False

    def integer(self):
        """Check if the input is an integer."""
        if re.match(r"^[-+]?([1-9]\d*|0)$", self.variable):
            return True
        return False

    def name(self):
        """Check if the input is a word."""
        if re.match(r"^[A-Za-z]{2,25}||\s[A-Za-z]{2,25}$", self.variable):
            return True
        return False


class Serializer:
    """This class serializes data."""

    @classmethod
    def serialize(cls, response, status_code, message=200):
        """Serializes data output."""
        if status_code in (400, 401, 403, 404, 405, 500):
            return json.dumps({
                "status": status_code,
                "message": message,
                "error": response
            }), status_code
        return json.dumps({
            "status": status_code,
            "message": message,
            "data": response
        }), status_code

    @classmethod
    def raise_error(cls, status, msg):
        """Display error message."""
        return json.dumps({
            "status": status,
            "message": msg
        }), status

    @classmethod
    def bad_request(cls, e):
        """Capture bad request error."""
        return json.dumps({
            "status": "400",
            "message": "bad request"
        }), 400

    @classmethod
    def page_not_found(cls, e):
        """Capture not found error."""
        return json.dumps({
            "status": "404",
            "message": "resource not found"
        }), 404

    @classmethod
    def method_not_allowed(cls, e):
        """Capture method not allowed error."""
        return json.dumps({
            "status": "405",
            "message": "method not allowed"
        }), 405

    @classmethod
    def internal_server_error(cls, e):
        """Capture internal server error."""
        return json.dumps({
            "status": "500",
            "message": "internal server error"
        }), 500


def admin_required(users):
    """This is a function.

    Args:
        users (dictionary): Return a array of user objects. A list of users in an array.

    Returns:
        json: Returns Json Object with a message if the user is unauthorized.
    """
    @wraps(users)
    def admin_rights(func):
        """This is a function.

        Args:
            func (function): The function takes another function as an argument.

        Returns:
            function: returns_rights function.
        """
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            """Interface to adapt to the existing codes, so as to save one from modifying thier codes back and forth. 

            Returns:
                function: Returns a function(func) that takes positional and key word arguments.
            """
            try:
                cur_user = [
                    user for user in users if user['email'] == get_jwt_identity()]
                user_role = cur_user[0]['role']
                if user_role != 'admin':
                    return {
                        'message': 'This activity can only be completed by the admin'}, 403  # Forbidden
                return func(*args, **kwargs)
            except Exception as e:
                return {"message": e}

        return wrapper_function
    return admin_rights
