from bottle import run, static_file, route, default_app
from playmaker import makepl, getjson

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@route('/make')
def maker():
    getjson()
    makepl()

app = default_app()