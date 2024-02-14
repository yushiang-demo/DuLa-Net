from flask import send_file
from flask_restx import Resource

from api.constant import STATIC_FOLDER
from api.app import app, api
from api.resources.task import Task as Task
from api.resources.admin.task import Task as AdminTask
from api.resources.admin.tasks import Tasks as AdminTasks

admin = api.namespace('admin', description='System info.')
admin.add_resource(AdminTasks, '/tasks')
admin.add_resource(AdminTask, '/task')

task = api.namespace('task', description='DuLa-Net task.')
task.add_resource(Task,'/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)