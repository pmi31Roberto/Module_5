import hashlib
import time


# Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


# Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
# adult_mode(ограничение по возрасту, bool (False по умолчанию))
class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = 0


# Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None


    def log_in(self, password, nickname):
        hash_password = hash(password)
        for i in self.users:
            if hash_password == i.users and nickname == i.users:
                self.current_user = i
                return
            print(f"Пользователь {nickname} не найден")

    def register(self, nickname, password, age):
        flag = False
        for i in self.users:
            if i.nickname == nickname:
                flag = True
                break
        if flag:
            print(f'Пользователь {nickname} уже существует')
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        self.current_user = None
        pass

    def add(self, *other):
        for i in other:
            flag = False
            for j in self.videos:
                if j.title == i.title:
                    print('В данном списке уже содержится один или несколько видеороликов из вашего списка')
                    flag = True
                    break
            if not flag:
                self.videos.append(i)

    def get_videos(self, word):
        list_video = []
        for i in self.videos:
            if word.lower() in i.title.lower():
                list_video.append(i.title)
        return list_video

    def watch_video(self, movie_title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        flag = False
        for i in self.videos:
            if i.title == movie_title:
                flag = True
                if i.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for j in range(i.time_now, i.duration):
                    print(j, end=' ')
                    time.sleep(1)
                    if j == i.duration - 1:
                        print('Конец видео')
        if not flag:
            print(f'Видео {movie_title} не найдено')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
