from flask import Flask, render_template, request, url_for, redirect
import sqlalchemy
from login import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        if form.username.data == '11111111' and form.password.data == '11111111':
            return redirect("/about")
        return 'not now, not yet'
    return render_template('login.html', title='Авторизация', form=form)



@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
