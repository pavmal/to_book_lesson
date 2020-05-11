import os
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import data

app = Flask(__name__)
SECRET_KEY = os.urandom(32)

@app.route('/')
def render_main():
    """
    Представление главной страницы
    :return: 'Здесь будет Главная страница'
    """

    return render_template('index.html')



@app.route('/about/')
def render_about():
    """
    Представление страницы "О сервисе"
    :return: Описание сервиса
    """
    return render_template('about.html')




if __name__ == '__main__':
    app.run('127.0.0.1', 8888, debug=False)
    #app.run()  # for gunicorn server

    toolbar = DebugToolbarExtension(app)