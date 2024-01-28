from flask import send_from_directory
from flask_restx import Resource

from api.constant import STATIC_FOLDER
from api.app import app, api
from api.resources import Task, Tasks

@app.route('/raw/<path:filename>')
def serve_static(path):
    return send_from_directory(STATIC_FOLDER, path)

admin = api.namespace('admin', description='Inspect system info.')
admin.add_resource(Tasks, '/tasks')

task = api.namespace('task', description='Run a DuLa-Net task.')
task.add_resource(Task,'/')

if __name__ == '__main__':
    app.run(debug=True)