import db
from cli.user_inputs import get_user_inputs

class UserDoesNotExist(Exception):
    def __init__(self, message):
        super().__init__(message)

class LoginException(Exception):
    def __init__(self, message):
        super().__init__(message)

def login():
    user_input = get_user_inputs({
        "username": "Enter username: ",
        "password": "Enter password: "
    })
    username, password = user_input.values()
    if not db.user_exists(username):
        raise UserDoesNotExist(f"Username {username} does not exist")
    user = db.get_user(username)
    if user and user.password == password:
        db.set_current_user(user)
    else:
        raise LoginException(f"Login failed for {username}")
