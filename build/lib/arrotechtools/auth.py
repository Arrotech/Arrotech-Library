from functools import wraps
from flask_jwt_extended import get_jwt_identity


def admin_required(users: list):
    """_summary_

    Args:
        users (list): _description_

    Returns:
        _type_: _description_
    """
    @wraps(users)
    def admin_rights(func):
        """_summary_

        Args:
            func (_type_): _description_

        Returns:
            _type_: _description_
        """
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            """_summary_

            Returns:
                _type_: _description_
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
