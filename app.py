from bottle import run, static_file, route, default_app
from playmaker import makepl, getjson

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@route('/make')
def maker():
    getjson()
    makepl()

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
else:
    app = default_app()