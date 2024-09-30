
from library_management.user import Librarian


def role_required(role):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if isinstance(self.logged_in_user, role):
                return func(self, *args, **kwargs)
            else:
                return None
        return wrapper
    return decorator
