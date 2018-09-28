from bottle import run, static_file, route, default_app
from playmaker import makepl, getjson

makepl()

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@route('/make')
def maker():
    getjson()
    makepl()

application = default_app()