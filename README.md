# Arrotechtools Library

## Installation

Install the latest version:

    pip install arrotechtools

To install a specific version:

    pip install arrotechtools==1.6

## Getting Started

After installation, you can immediately start using the library.

Importing a class, an object, or a method is straight forward.

Let simulate an import.

    from arrotechtools import Serializer, Validate, ErrorHandler, admin_required

## Validation

Supported validation inputs include:

1. Email
2. Password
3. Integer
4. Name
5. Phone:   `phone, airtel, safaricom, orange, equitel`

| method        | input type | sample |
| --------------|-----------|----------|
| email         | String    | test@gmail.com |
| password      | String    | HeuliaI!djvb24628 |
| integer       | Integer   | 23 `+ or -` are also accepted i.e `+25` or `-22` |
| name          | String    | John doe |
| phone, airtel, safaricom, orange, equitel | String | +254712345678 |

### Email validation Example

Lets begin with validating an email provided by a user.

    from arrotechtools import Validate, Serializer, ErrorHandler

    email = "your@gmail.com"

    if not Validate.email(email):
        return ErrorHandler.raise_error("invalid email format", 400)
    else:
        ...

Here, we are checking if the input is a valid email.

## Serializing data output

Seriale data.

    from arrotechtools import Serializer

    #Fetching data from a database or a data structure i.e list
    response = Users().get_users()
    ...
    if response:
        return Serializer.serialize(response, "Success", 200)
    else:
        ...

Here, we get records from the database and storing the data in a variable. Then we serialize the data into json object or an array.
The `serialize` object can serialize any different types data into json object(s). That includes `lists, dictionaries, or arrays`.

## Error Handling

Serialize errored responses:

    from arrotechtools import ErrorHandler, Validate

    name = "jane doe"
    ...
    if not Validate().name(name):
        return ErrorHandler.raise_error("Name is invalid", 400)
    else:
        ...

### Example 2

Lets a look at how we can capture errors at the entry point of a flask application.

    from flask import Flask
    from arrotechtools import Serializer

    app = Flask(__name__)
    ...

    #register error handlers
    app.register_error_handler(400, Serializer.bad_request)
    app.register_error_handler(404, Serializer.page_not_found)
    app.register_error_handler(405, Serializer.method_not_allowed)
    app.register_error_handler(500, Serializer.internal_server_error)

This is a straight forward way of handling errors in flask.

## Admin Protected Route

This is a function that takes an array of users as an argument and checks if the role is an admin.
If that isn't the case, the function returns an unauthorized status code and message.
Otherwise, the user is permitted to use the function.

### How to use the decorator to protect routes

    from arrotechtools import admin_required

    @jwt_required
    @admin_required(users)
    def signup():
        ...

The decorator takes a list of `users` as an argument.

## Support Team

    Email: arrotechdesign@gmail.com
    Phone: +254 711 371 265

## Author

    Harun Gachanja G.
