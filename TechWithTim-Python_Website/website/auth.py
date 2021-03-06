from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """ data = request.form
    print(data)"""
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return render_template("logout.html")

@auth.route("sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('email too short!', category="error")
        elif len(firstName) < 2:
            flash('First name too short!', category="error")
        elif password1 != password2:
            flash('Passwords don\'t match!', category="error")
        elif len(password1) < 7:
            flash('Password must be at least 7 characters!', category="error")
        else:
            flash('Acount created!', category="success")
    return render_template("sign_up.html")
