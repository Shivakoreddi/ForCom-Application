from flask import request,Flask,render_template,url_for,redirect,flash
from forms import RegistrationForm,LoginForm
import json
import sqlite3
import forum_db_connection as fd


app = Flask(__name__)

app.config['SECRET_KEY'] = 'd6b56b65c26cda9168d90a7d4237802c'

posts = [
    {
        "title":"Forum post 1",
        "author": "shiva Koreddi",
        "date_posted":"04/19/2021",
        "content":"First post content"

    },
    {
        "title":"Forum Post 2",
        "author": "Sravani",
        "date_posted": "04/19/2021",
        "content":"Second post content"

    }
]
class Forum():
    @app.route("/home")
    def home():
        return render_template('home.html',posts = posts)

    @app.route("/about")
    def about():
        return render_template('about.html')

    @app.route("/register",methods = ['GET','POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            flash(f'Account created for {form.username.data}!','success')
            return redirect(url_for('home'))
        return render_template('register.html', title='Register', form=form)

    @app.route("/login",methods=['GET','POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            if form.username.data=='admin' and form.password.data=='password':
                flash(f'You have been logged in', 'success')
                return redirect(url_for('home'))
            else:
                flash(f'Login Unsuccessful', 'danger')
        return render_template('login.html', title='Login', form=form)
if  __name__=="__main___":
    app.run(debug=True)