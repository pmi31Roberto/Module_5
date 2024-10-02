# Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


# Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
# adult_mode(ограничение по возрасту, bool (False по умолчанию))
class Video:

    def __init__(self, title, duration, adult_made=False, time_now=0):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_made
        self.time_now = time_now


# Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
class UrTube:

    def __init__(self, users, videos, current_user):
        pass

    def log_in(self, password, nickname):
        # if (password and nickname) in users:
        pass

    def register(self, nickname, password, age):
        pass

    def log_out(self):
        # self.nickname = None
        pass

    def __add__(self, *other):
        pass

    def get_videos(self, word):
        pass

    def watch_video(self, movie_title):
        pass


