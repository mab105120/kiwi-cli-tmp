from domain.User import User
from domain.Stock import Stock
from typing import Dict, List

users: Dict[str, User] = {
    "admin": User("admin", "adminpass","admin", "admin", 0.0)
}

_stocks: List[Stock] = [
    Stock("AAPL", "Apple Inc", 120.0),
    Stock("FB", "Meta Inc.", 80.0),
    Stock("GOOG", "Alphabet Inc.", 160.0),
    Stock("MSFT", "Microsoft Inc.", 202)
]

current_user = None

def query_all_stocks() -> List[Stock]:
    return _stocks

def get_current_user() -> User|None:
    return current_user

def set_current_user(user: User):
    global current_user
    current_user=user

def reset_current_user():
    global current_user
    current_user = None

def get_user(username: str) -> User|None:
    return users[username] if user_exists(username) else None

def add_user(user: User): 
    users[user.username] = user

def user_exists(username: str):
    try:
        users[username]
        return True
    except:
        return False

def delete_user(username: str):
    if user_exists(username):
        del users[username]

def get_all_users() -> List[User]:
    return list(users.values())