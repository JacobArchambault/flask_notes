from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from notes.models import db, User

registration_blueprint = Blueprint('registration', __name__, url_prefix='/registration/')

@registration_blueprint.route('/sign_up/', methods=('GET', 'POST'))
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username: 
            error = 'Username is required.'
        elif not password: 
            error = 'Password is required.'
        elif User.query.filter_by(username=username).first():
            error = 'Username is already taken.'
        
        if error is None:
            db.session.add(User(username=username, password=generate_password_hash(password)))
            db.session.commit()
            flash("Successfully signed up! Please log in.", 'success')
            return redirect(url_for('registration.log_in'))

        flash(error, 'error')
    form_post = url_for('registration.sign_up')
    anchor_link = url_for('registration.log_in')
    return render_template('log_in_form.html', action="Sign Up", prompt="Already have an account? Log In.", form_post=form_post, anchor_link=anchor_link)

@registration_blueprint.route('/log_in/', methods=('GET', 'POST'))
def log_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            error = 'Username or password are incorrect.'
        
        if error is None:
            session.clear()
            session['user_id'] = user.id 
            return redirect(url_for('index'))

        flash(error, 'error')
    form_post = url_for('registration.log_in')
    anchor_link = url_for('registration.sign_up')
    return render_template('log_in_form.html', action="Log In", prompt="Don't have an account? Sign Up.", form_post=form_post, anchor_link=anchor_link)

@registration_blueprint.route('/log_out/', methods=('GET', 'DELETE'))
def log_out():
    session.clear()
    flash('Successfully logged out.', 'success')
    return redirect(url_for('registration.log_in'))
