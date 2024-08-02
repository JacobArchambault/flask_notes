import functools
from flask import redirect, url_for, g

def require_login(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        return redirect(url_for('registration.log_in')) if not g.user else view(**kwargs)
    return wrapped_view

