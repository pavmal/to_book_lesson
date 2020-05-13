import os, json, random
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
SECRET_KEY = os.urandom(32)

@app.route('/')
def render_main():
    """
    Представление главной страницы
    :return: 'Здесь будет Главная страница'
    """
#    print(teachers[0]['name'])
    list_teachers = random.sample(teachers, k=6)
#    list_teachers = list_teachers.sort(key=lambda x: x['rating'])
    return render_template('index.html', list_goals=goals, list_teachers=list_teachers)


@app.route('/goals/<goal_id>/')
def render_goals(goal_id):
    """
    Представление страницы с преподавателями по направлениями
    :return: 'Здесь будет список преподавателей с учетом направлений'
    """
 #   print(request.path)
    goal_id = request.path.split('/')[-2]
    one_goal = {key: val for key, val in goals.items() if key == goal_id}
    short_list_teachers = [teacher for teacher in teachers if goal_id in teacher['goals']]

#    goal_teachers = {key: depart for key, depart in data.departures.items() if key == direct}
#    short_list_tours = {num: tour for num, tour in data.tours.items() if tour['departure'] == direct}
    print(goal_id)
    print(one_goal)
    print(len(short_list_teachers))
    return render_template('goal.html', list_goals=one_goal, list_teachers=short_list_teachers)


@app.route('/profiles/<teacher_id>/')
def render_teachers(teacher_id):
    """
    Представление страницы с профилем преподавателя
    :return: 'Здесь будет профиль преподавателя'
    """
 #   print(request.path)
    teacher_id = request.path.split('/')[-2]
    one_teacher = [teacher for teacher in teachers if teacher['id'] == int(teacher_id)]
    short_list_goals = {key: goal for key, goal in goals.items() if key in one_teacher[0]['goals']}
    list_free = []
    Mon = [hour for hour, val in one_teacher[0]['free']['mon'].items() if val == True]
    list_free.append({'Понедельник': Mon})
    Tue = [hour for hour, val in one_teacher[0]['free']['tue'].items() if val == True]
    list_free.append({'Вторник': Tue})
    Wed = [hour for hour, val in one_teacher[0]['free']['wed'].items() if val == True]
    list_free.append({'Среда': Wed})
    Thu = [hour for hour, val in one_teacher[0]['free']['thu'].items() if val == True]
    list_free.append({'Четверг': Thu})
    Fri = [hour for hour, val in one_teacher[0]['free']['fri'].items() if val == True]
    list_free.append({'Пятница': Fri})
    Sat = [hour for hour, val in one_teacher[0]['free']['sat'].items() if val == True]
    list_free.append({'Суббота': Sat})
    Sun = [hour for hour, val in one_teacher[0]['free']['sun'].items() if val == True]
    list_free.append({'Воскресенье': Sun})

    for elem in list_free:
        for k, v in elem.items():
            print(k, v)
    print(list_free)
    return render_template('profile.html', list_goals=short_list_goals, list_teachers=one_teacher, schedule=list_free)


@app.route('/about/')
def render_about():
    """
    Представление страницы "О сервисе"
    :return: Описание сервиса
    """
    return render_template('about.html')




if __name__ == '__main__':
#    with open('goals.txt', 'w') as f:
#        json.dump(data.goals, f)

    with open('goals.txt', 'r') as f:
        goals = json.load(f)
    with open('teachers.txt', 'r') as f:
        teachers = json.load(f)
#    print(goals)
#    print(teachers)

#    for t in teachers:
 #           print(t['free']['mon'])

#    list_teachers = teachers.sort(key=lambda x: x[0]['rating'])
#    print(list_teachers)

    app.run('127.0.0.1', 7788, debug=True)
    #app.run()  # for gunicorn server

    toolbar = DebugToolbarExtension(app)