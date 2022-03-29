import re


class Validate:
    """Class with validation methods.
    """

    def __init__(self):
        """Class constructor.
        """

    @classmethod
    def email(cls, variable: str):
        """_summary_

        Args:
            variable (_type_): _description_

        Returns:
            _type_: _description_
        """
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$)",
                    variable):
            return True
        return False

    @classmethod
    def password(cls, variable: str):
        """_summary_

        Args:
            variable (str): _description_

        Returns:
            _type_: _description_
        """
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", variable):
            return True
        return False

    @classmethod
    def phone(cls, variable: str):
        """_summary_

        Args:
            variable (str): _description_

        Returns:
            _type_: _description_
        """
        if re.match(r"^(?:254|\+254|0)?(7(?:(?:[129][0-9])|(?:0[0-8])|(4[0-1]))[0-9]{6})$", variable):
            return True
        return False

    @classmethod
    def safaricom(cls, variable: str):
        """_summary_

        Args:
            variable (str): _description_

        Returns:
            _type_: _description_
        """
        if re.match(r"^(?:254|\+254|0)?(7(?:(?:[129][0–9])|(?:0[0–8])|(4[0–1]))[0–9]{6})$", variable):
            return True
        return False

    @classmethod
    def airtel(cls, variable: str):
        """_summary_

        Args:
            variable (str): _description_

        Returns:
            _type_: _description_
        """
        if re.match(r"^(?:254|\+254|0)?(7(?:(?:[3][0-9])|(?:5[0-6])|(8[0-9]))[0-9]{6})$", variable):
            return True
        return False

    @classmethod
    def orange(cls, variable: str):
        """_summary_

        Args:
            variable (str): _description_

        Returns:
            _type_: _description_
        """
        if re.match(r"^(?:254|\+254|0)?(77[0-6][0-9]{6})$", variable):
            return True
        return False

    @classmethod
    def equitel(cls, variable):
        """_summary_

        Args:
            variable (_type_): _description_

        Returns:
            _type_: _description_
        """
        if re.match(r"^(?:254|\+254|0)?(76[34][0-9]{6})$", variable):
            return True
        return False

    @classmethod
    def integer(cls, variable: int):
        """_summary_

        Args:
            variable (int): _description_

        Returns:
            _type_: _description_
        """
        if re.match(r"^[-+]?([1-9]\d*|0)$", variable):
            return True
        return False

    @classmethod
    def name(cls, variable: str):
        """_summary_

        Args:
            variable (str): _description_

        Returns:
            _type_: _description_
        """
        if re.match(r"^[A-Za-z]{2,25}||\s[A-Za-z]{2,25}$", variable):
            return True
        return False
