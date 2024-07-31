from flask import Blueprint, render_template, redirect, url_for, request, session, flash, g
from notes.authorization.require_login import require_login
from notes.models import db, Note

bp = Blueprint('notes', __name__, url_prefix='/notes')

@bp.route('/new', methods=('GET', 'POST'))
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
            return redirect(url_for('note_index'))

        flash(error, 'error')
    form_post = url_for('notes.note_create')
    return render_template('note_form.html', header="New Note", form_post=form_post, button_value="Create Note", title="", body="")
