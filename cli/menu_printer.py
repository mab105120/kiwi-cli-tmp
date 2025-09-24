from typing import Dict
from domain.MenuFunctions import MenuFunctions
from rich.console import Console
from rich.table import Table
import constants
import sys
import db
from services.login_service import login
from services.user_service import create_user, get_users, delete_user

_console = Console()

_menus: Dict[int, str] = {
    constants.LOGIN_MENU: "----\nWELCOME TO KIWI\n----\n1. Login\n0. Exit",
    constants.MAIN_MENU: "----\nMAIN MENU\n----\n1. Manage users\n2. My portfolios\n3. Marketplace\n0. Logout",
    constants.MANAGE_USERS_MENU: "----\nUSERS MENU\n----\n1. View users\n2. Create user\n3. Delete user\n0. Back to main menu"
}

def print_user_manager_menu():
    current_user = db.get_current_user()
    if current_user and current_user.username == "admin":
        return constants.MANAGE_USERS_MENU
    else:
        print_error(f"User is not authorized to perform this operation")
        return constants.MAIN_MENU

def print_user_table(users):
    tbl = Table()
    tbl.add_column(header="Username")
    tbl.add_column(header="Name")
    tbl.add_column(header="Balance")
    for user in users:
        tbl.add_row(user.username, f"{user.lastname}, {user.firstname}", str(user.balance))
    _console.print(tbl)



_router: Dict[str, MenuFunctions] = {
    "0.1": MenuFunctions(executor=login, navigator=lambda: 1),
    "1.1": MenuFunctions(navigator=print_user_manager_menu),
    "2.1": MenuFunctions(executor=get_users, printer=print_user_table),
    "2.2": MenuFunctions(executor=create_user),
    "2.3": MenuFunctions(executor=delete_user)
}

def print_menu(menu_id: int):
    _console.print(_menus[menu_id])
    user_selection = int(_console.input(">> "))
    handle_user_selection(menu_id, user_selection)

def print_error(error: str):
    _console.print(error, style="red")

def handle_user_selection(current_menu_id: int, user_selection: int):
    if user_selection == 0:
        if current_menu_id == constants.LOGIN_MENU:
            sys.exit(0)
        elif current_menu_id == constants.MAIN_MENU:
            db.reset_current_user()
            print_menu(constants.LOGIN_MENU)
        else:
            print_menu(constants.MAIN_MENU)
    formatted_user_selection = f"{current_menu_id}.{user_selection}"
    try: 
        menu_functions = _router[formatted_user_selection]
        if menu_functions.executor:
            result = menu_functions.executor()
            if result:
                menu_functions.printer(result) if menu_functions.printer else _console.print(result)
        print_menu(menu_functions.navigator()) if menu_functions.navigator else print_menu(current_menu_id)       
    except KeyError as ke:
        print_error(f"Invalid user selection: {str(ke)}")
        print_menu(current_menu_id)
    except Exception as e:
        print_error(f"Error: {str(e)}")
        print_menu(current_menu_id)
