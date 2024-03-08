from flask import Flask, render_template, request, url_for, redirect

from login import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.submit():
        print('sdljfkjsds')
    print(form.username.data)
    print(form.password.data)
    return render_template('login.html', title='Авторизация', form=form)



@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
