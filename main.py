import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QFont, QPixmap
import datetime
from apis.weather import get_weather
from apis.news import get_posts

location = 'Ulsan'


class MyApp(QWidget):

    def __init__(self, size):
        super().__init__()
        # print(size.width())
        # 가로세로 옵션이 달라서 고려해줘야 할듯
        self.screen_width = size.width()
        self.screen_height = size.height()
        print("Screen Width : {} \nScreen Height: {}".format(self.screen_width, self.screen_height))
        self.initUI()

    def initUI(self):
        total = QVBoxLayout()
        self.setLayout(total)
        self.setStyleSheet("background-color: black")

        v_clock = self.clock_widget()
        v_weather = self.weather_widget()
        v_news = self.news_widget()

        top_wrap = QHBoxLayout()
        top_wrap.addStretch(1)
        top_wrap.addLayout(v_clock)
        top_wrap.addStretch(5)
        top_wrap.addLayout(v_weather)
        top_wrap.addStretch(1)

        news_wrap = QHBoxLayout()
        news_wrap.addStretch(1)
        news_wrap.addLayout(v_news)
        news_wrap.addStretch(1)
        total.addStretch(1)
        total.addLayout(top_wrap)
        total.addStretch(5)
        total.addLayout(news_wrap)
        total.addStretch(2)

        self.setWindowTitle('Suwan\'s Mirror')
        self.show()

    def news_widget(self):
        news_img = QLabel()
        pixmap = QPixmap('assets/Newspaper.png')
        pixmap = pixmap.scaled(50, 50)
        news_img.setPixmap(pixmap)

        posts = get_posts()
        news_box = QVBoxLayout()
        news_box.addWidget(news_img)

        for index, post in enumerate(posts):
            post = QLabel(post)
            post.setStyleSheet("color: white")
            post.setFont(QFont("Times", 14))
            news_box.addWidget(post)

        return news_box

    def weather_widget(self):
        v_weather = QVBoxLayout()
        temp, weather, icon = get_weather(location)

        l_weather_img = QLabel()

        pixmap = QPixmap(icon)
        pixmap = pixmap.scaled(100, 100)
        l_weather_img.setPixmap(pixmap)

        ment = "{}도 {}".format(temp, weather)
        l_temp = QLabel(ment)
        l_temp.setStyleSheet("color: white")
        l_temp.setFont(QFont("Times", 20))

        v_weather.addWidget(l_weather_img)
        v_weather.addWidget(l_temp)

        return v_weather

    def clock_widget(self):
        year = datetime.date.today().year
        month = datetime.date.today().month
        day = datetime.date.today().day
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        weekday = datetime.datetime.today().strftime('%A')

        v_clock = QVBoxLayout()

        l_time = QLabel("{}:{}".format(str(hour), str(minute)))
        l_time.setStyleSheet("color: white")
        l_time.setFont(QFont("Times", 70))

        l_day = QLabel("{}년 {}월 {}일 {}".format(year, month, day, weekday))
        l_day.setStyleSheet("color: white")
        l_day.setFont(QFont("Times", 20))

        v_clock.addWidget(l_time)
        v_clock.addWidget(l_day)

        return v_clock


if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    ex = MyApp(size)
    ex.showFullScreen()
    sys.exit(app.exec_())
