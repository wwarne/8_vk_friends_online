import vk
from getpass import getpass


APP_ID = 5914902


def get_user_login():
    return input('Enter login: ')


def get_user_password():
    return getpass(prompt='Enter password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friends_ids = api.friends.getOnline()
    return api.users.get(user_ids=friends_ids, fields='first_name, last_name')


def output_friends_to_console(friends_online):
    if not friends_online:
        print('No friends online found')
    else:
        print('Friends online:')
        for my_friend in friends_online:
            print('{} {}'.format(my_friend['first_name'], my_friend['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
