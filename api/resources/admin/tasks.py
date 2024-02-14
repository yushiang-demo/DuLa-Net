import os
from flask_restx import Resource

from api.constant import STATIC_FOLDER
from api.app import api
from api.models import Tasks
from mongodb.app import db

class Tasks(Resource):
    @api.marshal_with(Tasks)
    def get(self):
        tasks = db.getTasks()
        return { "tasks": tasks }, 200
            