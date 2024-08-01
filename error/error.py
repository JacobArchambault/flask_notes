from flask import Blueprint, render_template

def page_not_found(e):
    return render_template('404.html'), 404