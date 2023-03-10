import typing

from .models import User

def find_user_by_username(username: str) -> typing.Optional[User]:
    user = User.objects.filter(username=username)
    if user.exists():
        return user.first()
    else:
        return None
        