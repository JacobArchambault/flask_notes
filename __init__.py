import os
from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from flask_migrate import Migrate 
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv, find_dotenv
from notes.notes import bp
from .models import db, User
load_dotenv(find_dotenv())

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    

    db.init_app(app)
    migrate = Migrate(app, db)

    @app.errorhandler(404)
    def page_note_found(e):
        return render_template('404.html'), 404

    @app.before_request
    def load_user():
        user_id = session.get('user_id')
        g.user = User.query.get(user_id) if user_id else None

    @app.route('/sign_up/', methods=('GET', 'POST'))
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
                return redirect(url_for('log_in'))

            flash(error, 'error')
        form_post = url_for('sign_up')
        anchor_link = url_for('log_in')
        return render_template('log_in_form.html', action="Sign Up", prompt="Already have an account? Log In.", form_post=form_post, anchor_link=anchor_link)

    @app.route('/log_in/', methods=('GET', 'POST'))
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
        form_post = url_for('log_in')
        anchor_link = url_for('sign_up')
        return render_template('log_in_form.html', action="Log In", prompt="Don't have an account? Sign Up.", form_post=form_post, anchor_link=anchor_link)

    @app.route('/log_out/', methods=('GET', 'DELETE'))
    def log_out():
        session.clear()
        flash('Successfully logged out.', 'success')
        return redirect(url_for('log_in'))

    @app.route('/')
    def index():
        return redirect(url_for('notes.note_index'))

    app.register_blueprint(bp)
    return app