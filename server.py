from flask import send_file
from flask_restx import Resource

from api.constant import STATIC_FOLDER
from api.app import app, api
from api.resources import Task, Tasks

admin = api.namespace('admin', description='System info.')
admin.add_resource(Tasks, '/tasks')

task = api.namespace('task', description='DuLa-Net task.')
task.add_resource(Task,'/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)