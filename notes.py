from flask import Blueprint, render_template, redirect, url_for, request, session, flash, g
from notes.authorization.require_login import require_login
from notes.models import db, Note
from notes.authorization.before_request import load_user

note_blueprint = Blueprint('notes', __name__, url_prefix='/notes/')
note_blueprint.before_request(load_user)

@note_blueprint.route('/')
@require_login
def note_index():
    return render_template('note_index.html', notes=g.user.notes)

@note_blueprint.route('/new/', methods=('GET', 'POST'))
@require_login
def note_create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title: 
            error = 'Title is required.'
        
        if error is None:
            note = Note(author=g.user, title=title, body=body)
            db.session.add(note)
            db.session.commit()
            flash(f"Successfully created note: {title}", 'success')
            return redirect(url_for('notes.note_index'))

        flash(error, 'error')
    form_post = url_for('notes.note_create')
    return render_template('note_form.html', header="New Note", form_post=form_post, button_value="Create Note", title="", body="")

@note_blueprint.route('/<note_id>/edit/', methods=('GET', 'POST', 'PATCH', 'PUT'))
@require_login
def note_update(note_id):
    note = Note.query.filter_by(user_id=g.user.id, id=note_id).first_or_404()

    if request.method in ['POST', 'PATCH', 'PUT']:
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title: 
            error = 'Title is required.'

        if error is None:
            note.title = title
            note.body = body
            db.session.add(note)
            db.session.commit()
            flash(f"Successfully updated note: {title}", 'success')
            return redirect(url_for('notes.note_index'))

        flash(error, 'error')

    title = note.title
    body = note.body
    form_post = url_for('notes.note_update', note_id=note.id)
    return render_template('note_form.html', note=note, header=f"Edit Note: {title}", form_post=form_post, button_value="Update Note", title=title, body=body)

@note_blueprint.route('/<note_id>/delete/', methods=('GET', 'DELETE'))
@require_login
def note_delete(note_id):
    note = Note.query.filter_by(user_id=g.user.id, id=note_id).first_or_404()
    db.session.delete(note)
    db.session.commit()
    flash(f"Successfully deleted note: '{note.title}'", 'success')
    return redirect(url_for('notes.note_index'))