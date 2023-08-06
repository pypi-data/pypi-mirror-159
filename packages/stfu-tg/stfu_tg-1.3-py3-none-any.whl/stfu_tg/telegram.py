from .formatting import Url


class UserLink(Url):
    user_id: int

    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.link = f'tg://user?id={user_id}'
        self.name = name
