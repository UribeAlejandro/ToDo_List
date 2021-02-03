from flask_sqlalchemy import SQLAlchemy
from forms.forms import RegistrationForm, LogInForm
from flask import Flask, render_template, url_for, flash, redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = '517cf09a279eea867458709ec5c043cc'
app.config['SQALCHEMY_DATABASE_URI'] = 'sqlite:///data/site.db'

db = SQLAlchemy(app)

posts = [
    {
        "title": "Blog1",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ultrices congue nisi eu "
                   "congue. Morbi sapien ante, scelerisque eu mollis id, vulputate sed lorem. Praesent iaculis ex "
                   "lorem, in condimentum lectus feugiat eu. Donec a posuere orci, et mollis nulla. Fusce id nulla "
                   "egestas elit laoreet vulputate. Vivamus tristique ex nec turpis rutrum gravida. Maecenas sodales "
                   "leo libero, at feugiat nisl accumsan sit amet. Nulla vel nunc risus. Lorem ipsum dolor sit amet, "
                   "consectetur adipiscing elit. Praesent eu purus euismod, accumsan mauris id, luctus eros. Praesent "
                   "in felis vitae justo aliquam hendrerit. Quisque sit amet efficitur sapien.",
        "author": "Author 1",
        "date_posted": "Date 1"
    },
    {
        "title": "Blog2",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ultrices congue nisi eu "
                   "congue. Morbi sapien ante, scelerisque eu mollis id, vulputate sed lorem. Praesent iaculis ex "
                   "lorem, in condimentum lectus feugiat eu. Donec a posuere orci, et mollis nulla. Fusce id nulla "
                   "egestas elit laoreet vulputate. Vivamus tristique ex nec turpis rutrum gravida. Maecenas sodales "
                   "leo libero, at feugiat nisl accumsan sit amet. Nulla vel nunc risus. Lorem ipsum dolor sit amet, "
                   "consectetur adipiscing elit. Praesent eu purus euismod, accumsan mauris id, luctus eros. Praesent "
                   "in felis vitae justo aliquam hendrerit. Quisque sit amet efficitur sapien.",
        "author": "Author 2",
        "date_posted": "Date 2"
    }
]


@app.route('/')
@app.route('/home/')
def home():
    return render_template('index.html', title='Home', posts=posts)


@app.route('/about/')
def about():
    return render_template('about.html', title='About')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == "root@root.com" and form.password.data == "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Logging unsuccessful. Please check your username and password.', 'danger')
    return render_template('login.html', title='Log In', form=form)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
