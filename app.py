from flask import Flask, render_template, url_for

app = Flask(__name__)

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
    return render_template('index.html', title="Home", posts=posts)


@app.route('/about/')
def about():
    return render_template('about.html', title="About")


@app.route('/login/')
def login():
    return render_template('login.html', title="Log In")


@app.route('/register/')
def register():
    return render_template('register.html', title="Register")


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
