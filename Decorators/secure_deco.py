import functools

user = {"username": "jose", "access_level": "admin"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_fuction(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}."

        return secure_fuction
    return decorator


@make_secure("admin")
def get_admin_password():
    return "admin: 1234"

print(get_admin_password())