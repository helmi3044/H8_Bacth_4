from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()