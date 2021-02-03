from flask_wtf import FlaskForm


class Registration(FlaskForm):
    def __init__(self):
        super(Registration).__init__()

    def foo(self):
        pass
