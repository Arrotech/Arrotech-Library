## Installation

You can install the library with the following command:

`pip install arrotechtools`

## Getting Started

After installation, you can immediately start using the library.

Importing a class, an object, or a method is straight forward.

Let simulate an import.

```
from arrotechtools import Validators, Serializer, admin_required
```

`Validators` and `Serializer` are classes while `admin_required` is a method.

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


**Email validation**

Lets begin with validating an email provided by a user. 

```
from arrotechtools import Validators, Serializer

email = "your@gmail.com"
...
if not Validators(email).email():
    return Serializer.raise_error(400, "invalid email format")
else:
    ...
```

Here, we are checking if the input is a valid email. In this case, the class `Validators` takes an email as an argument to validate against. 

**Phone validation**

Lets take a look at another example. This time round we will try to validate user phone number.

```
from arrotechtools import Validators, Serializer

phone = "your@gmail.com"
...
if not Validators(phone).safaricom():
    return Serializer.raise_error(400, "invalid email format")
else:
    ...
```
Here, we are checking if the input is a valid safaricom phone number. In this case, the class `Validators` takes the phone number as an argument to validate against.

## Serializing data output

```
from arrotechtools import Serializer

#Fetching data from a database or a data structure i.e list
response = Users().get_users()
...
if response:
    return Serializer.serialize(response, 200, "Success")
else:
    ...
```
Here, we are fetch some data from a database and storing the data in a variable `response`. Then we serialize the data into json object or an array.
The `serialize` object can serialize any different types data into json object(s). That includes `lists, dictionaries, or arrays`.

### Serialize error messages

```
from arrotechtools import Serializer, Validators

name = "jane doe"
...
if not Validators(name).name():
    return Serializer.raise_error(400, "Name is invalid")
else:
    ...
```

The method raise_error takes `status code` and `error meassage` as arguments.
We are simply validating the name provided by the user. If the name is not a word, then the function will return an error message and an appropriate status code.

### Error handling

With the `Serializer` class, you can handle errors accross your application.
Errors captured include:

1. Bad Request: `bad_request`

    ```
    message: "bad request",
    status: "400"
    ```
2. Resourse not found: `page_not_found`

    ```
    message: "resource not found",
    status: "404"
    ```
4. Method not allowed: `method_not_allowed`

    ```
    message: "method not allowed",
    status: "405"
    ```
4. Internal Server Error: `internal_server_error`

    ```
    message: "internal server error",
    status: "500"
    ```
**#Example 1**

Below is an example illustrating how to use the `page_not_found` object to capture exceptions as a result non-existing resources.

```
from arrotechtools import Serializer

#Fetch an item from a database or data structure i.e list
response = User().get_user_by_id(id)

if response:
    ...
else:
    return Serializer.page_not_found()
```

**#Example 2**

Lets a look at how we can capture errors at the entry point of a flask application.

```
from flask import Flask
from arrotechtools import Serializer

app = Flask(__name__)
...

#register error handlers
app.register_error_handler(400, Serializer.bad_request)
app.register_error_handler(404, Serializer.page_not_found)
app.register_error_handler(405, Serializer.method_not_allowed)
app.register_error_handler(500, Serializer.internal_server_error)
```
This is a straight forward way of handling errors in flask.

## Admin Protected Route

This is a function that takes an array of users as an argument and checks if the role is an admin.
If that isn't the case, the function returns an unauthorized status code and message. 
Otherwise, the user is permitted to use the function.

## How to use the decorator to protect routes

**example:**

```
from arrotechtools import admin_required


@jwt_required
@admin_required(users)
def signup():
    ...
```

The decorator takes a dictionary of `users` as an argument.

## Support Team

    Email: arrotechdesign@gmail.com
    Phone: +254 711 371 265

## Author

    Harun Gachanja G.
