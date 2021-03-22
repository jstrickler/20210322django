import requests

USER_NAME = 'joeschmoe'
USER_PASSWORD = 'b00lab00la'

HOST = "http://127.0.0.1:8000/"

TOKEN_URL = f"{HOST}auth/token/"
LOGIN_URL = f"{TOKEN_URL}login"
LOGOUT_URL = f"{TOKEN_URL}logout"

USER_URL = f"{HOST}auth/users/"
PROFILE_URL = f"{USER_URL}me"

CONTACTS_URL = f"{HOST}api/contacts"

def main():
    result = register_user(USER_NAME, USER_PASSWORD)
    print("REGISTER:", result)

    profile = get_user_profile()
    print("PROFILE:", profile)

    auth_token = login(USER_NAME, USER_PASSWORD)
    print("AUTH_TOKEN:", auth_token)

    profile = get_user_profile(auth_token)
    print("PROFILE:", profile)

    contacts = get_contact_list(auth_token)
    print("CONTACTS:", contacts)

    result = logout(auth_token)
    print("LOGOUT:", result)

    contacts = get_contact_list(auth_token)
    print("CONTACTS:", contacts)

def register_user(username, password):
    response = requests.post(
        USER_URL,
        data = {
            'username': username,
            'password': password,
        }
    )
    return response.json()

def get_user_profile(auth_token=None):
    if auth_token:
        headers = {'Authorization': f"Token {auth_token}"}
    else:
        headers = {}
    response = requests.get(PROFILE_URL, headers=headers)
    return response.json()

def login(username, password):
    response = requests.post(
        LOGIN_URL,
        data={
            'username': username,
            'password': password,
        }

    )
    return response.json()['auth_token']

def logout(auth_token):
    headers = {'Authorization': f"Token {auth_token}"}

    response = requests.post(
        LOGOUT_URL, headers=headers
    )
    return response.content

def get_contact_list(auth_token):
    headers = {'Authorization': f"Token {auth_token}"}

    response = requests.get(
        CONTACTS_URL,
        headers=headers
    )
    return response.content

if __name__ == '__main__':
    main()
