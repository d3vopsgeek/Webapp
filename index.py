from flask import Flask, render_template, redirect, url_for, request, flash, session
import os

app = Flask(__name__)


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
    # return redirect(url_for('index'))
    return home()


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
