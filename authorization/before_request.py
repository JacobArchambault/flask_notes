from flask import session, g
from notes.models import User

def load_user():
    user_id = session.get('user_id')
    g.user = User.query.get(user_id) if user_id else None
