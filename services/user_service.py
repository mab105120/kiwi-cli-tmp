from cli.user_inputs import get_user_inputs
import db
from domain.User import User
from typing import List
from domain.User import User

class UniqueUsernameException(Exception):
    def __init__(self, message):
        super().__init__(message)

class UnsupportedActionException(Exception):
    def __init__(self, message):
        super().__init__(message)

def get_users() -> List[User]:
    return db.get_all_users()

def delete_user():
    user_inputs = get_user_inputs({
        "username": "Enter username: "
    })
    username, = user_inputs.values()
    if username == "admin":
        raise UnsupportedActionException("Deleting admin user is not allowed")
    db.delete_user(username)

def create_user() -> str:
    user_inputs = get_user_inputs({
        "username": "Enter username: ",
        "password": "Enter password: ",
        "firstname": "Enter first name: ",
        "lastname": "Enter last name: ",
        "balance": "Enter balance: "
    })
    username, password, firstname, lastname, balance = user_inputs.values()
    if db.user_exists(username):
        raise UniqueUsernameException(f"{username} already exists. Username must be unique")
    user = User(username, password, firstname, lastname, float(balance))
    db.add_user(user)
    return "User created successfully"
