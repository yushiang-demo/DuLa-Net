import os
from flask import request
from flask_restx import Resource

from api.constant import TASK_STATUS
from api.app import api
from mongodb.app import db

class Task(Resource):
    def put(self):
        data = request.json
        id = data['id']
        db.updateTask(id, {
            'layout': data
        })
        if db.getTask(id):
            db.updateTask(id, {
                'status': TASK_STATUS.DONE,
            })

        return { "tasks": data }, 200