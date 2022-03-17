from flask import Flask, flash, render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def log_and_reg():
    return render_template('log_reg.html')

@app.route('/register/user', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    register_data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : pw_hash
    }
    print(request.form)
    print(register_data)
    user_id = User.register_user(register_data)
    session['user_id'] = user_id
    print(session['user_id'])
    return redirect('/dashboard')

@app.route('/dashboard')
def dashbord():
    user_data = {
        "id" : session['user_id']
    }
    return render_template('dashboard.html', user=User.get_user_by_id(user_data))





    