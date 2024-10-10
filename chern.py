import time


# [User(nickname=user1, password=<хэш пароля>, age=25),
# User(nickname=user2, password=<хэш пароля>, age=30), User(nickname=user3, password=<хэш пароля>, age=20)]
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = hash(password)
        for i in self.users:
            if i.nickname == nickname and i.password == hashed_password:
                self.current_user = i
                return
        print("Пользователь не найден")

    def register(self, nickname, password, age):
        user_exists = False
        for user in self.users:
            if user.nickname == nickname:
                user_exists = True
                break

        if user_exists:
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            video_exists = False
            for v in self.videos:
                if v.title == video.title:
                    video_exists = True
                    break
            if not video_exists:
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        matching_videos = []
        for video in self.videos:
            if search_word in video.title.lower():
                matching_videos.append(video.title)
        return matching_videos

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        video_found = False
        for video in self.videos:
            if video.title == title:
                video_found = True
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Просмотр видео '{title}' начинается с {video.time_now} секунды")
                for i in range(video.time_now, video.duration):
                    print(f"Просмотр на {i} секунде")
                    time.sleep(1)
                print("Конец видео")
                video.time_now = 0
                break

        if not video_found:
            print(f"Видео '{title}' не найдено")


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
