from bottle import run, static_file, route, default_app
from playmaker import makepl

makepl()

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@route('/make')
def maker():
    makepl()
    
run(host='0.0.0.0', port=8080, debug=True, reloader=True)