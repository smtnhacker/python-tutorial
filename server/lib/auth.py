import os

ADMIN_USER = os.environ.get("ADMIN_USER")
ADMIN_PASS = os.environ.get("ADMIN_PASS")
ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN")

NORM_USER = os.environ.get("NORM_USER")
NORM_PASS = os.environ.get("NORM_PASS")

# wow! so secure
user_id = 0 
authenticated_users = dict()

def get_user_id(username):
    global authenticated_users
    global user_id
    
    if username in authenticated_users:
        return authenticated_users[username]
    new_user_id = str(user_id)
    user_id += 1
    authenticated_users[username] = new_user_id
    return new_user_id

def authenticate_user(username: str, password: str):
    # for this, there are only 2 roles
    if username == ADMIN_USER and password == ADMIN_PASS:
        return ADMIN_TOKEN
    
    if username.startswith(f"{NORM_USER}_") and password == NORM_PASS:
        real_username = username.split("_", maxsplit=1)[1]
        return get_user_id(real_username)

    return None