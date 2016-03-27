from flask import render_tempalte
from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')
