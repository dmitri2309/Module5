import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        return f'{self.nickname}'

    def __hash__(self):
        return hash(self.password)


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f'{self.title}'


class UrTube:
    users = []
    videos = []
    current_user = None

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        for i in self.users:
            if i.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        self.users.append(user)
        self.log_in(nickname, password)

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i
                return self.current_user

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for i in video:
            if i.title in self.videos:
                continue
            self.videos.append(i)
        return self.videos

    def get_videos(self, word):
        self.found_videos = []
        for j in self.videos:
            if word.lower() in j.title.lower():
                self.found_videos.append(j)
        return self.found_videos

    def watch_video(self, title):
        for i in self.videos:
            if title == i.title:
                if self.current_user is None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                elif i.adult_mode is True and self.current_user.age < 18:
                    print('Вам нет 18 пожалуйста покиньте страницу')
                else:
                    while i.time_now < i.duration:
                        i.time_now += 1
                        print(i.time_now, end='')
                    print(' Конец видео')
                    time.sleep(1)


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

# print(ur.videos)

print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# print(ur.users)

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')
