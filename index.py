from flask import Flask, render_template, redirect, url_for, request, flash, session, make_response
import os
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:123456@localhost:5432/isac"
Bootstrap(app)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/')
def home():
    # f not session.get('logged_in'):
    #    return render_template('home.html')
    # else:
    if 'username' in session:
        username = session['username']
        return 'logged as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
    else:
        return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        return '<h2>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h2>'
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            flash('Wrong Credentials!')
        else:
            session['logged_in'] = True
            session['username'] = 'admin'
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/logout")
def logout():
    # session['logged_in'] = False
    # session['username'] = None
    session.pop('username', None)
    session.pop('logged_in', None)
    return redirect(url_for('home'))


@app.route("/locations")
def locations():
    return render_template('locations.html')


@app.route("/reglocations", methods=['POST'])
def reply():
    return render_template('locations.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)
