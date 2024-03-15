from flask import Flask, render_template, request, url_for, redirect
import sqlalchemy

from data import db_session
from db_functions import create_user
from login import LoginForm
from utilites import check_password

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        if check_password(form.username.data, form.password.data):
            return redirect("/about")
        return 'not now, not yet'
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/registration')
def registration():
    return render_template('about.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    db_session.global_init("db/sport.db")
    create_user('superLogin', '12345678', name='Иван')
    app.run(debug=True)
