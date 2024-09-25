class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, с атрибутами: логин м пароль
    """

    def __init__(self, username, password, password_conf):
        self.username = username
        flag1 = False
        flag2 = False
        if len(password) >= 8:
            for i in password:
                if i.isupper():
                    flag1 = True
                    break
            for i in password:
                if i.isnumeric():
                    flag2 = True
                    break
            if flag1 and flag2:
                self.password = password
            else:
                print("Пароль должен содержать хотя бы 1 заглавную букву и хотя бы 1 цифру")
        else:
            print('Пароль должен содержать >= 8 символам')


if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('приветствую! выберите действие: \n1 - Вход\n2 - Регистрация\n')
        user = User(input("Логин: "), password1 := input("Пароль: "), password2 := input("Повтор пароля: "))
        if password1 != password2:
            print('Пароли должны совпадать!')
            exit()
        database.add_user(user.username, user.password)
        print(database.data)
