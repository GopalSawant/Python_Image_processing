user1 = {
    'name': 'Gopal',
    'valid': True
}


def authenticated(func):
    def wrapper(*args):
        if args[0]['valid']:
            return func(*args)

    return wrapper


@authenticated
def message_friend(user):
    print('message has been sent')


message_friend(user1)
