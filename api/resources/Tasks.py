import os
from flask_restx import Resource

from api.constant import STATIC_FOLDER
from api.app import api
from api.models import Tasks

class Tasks(Resource):
    @api.marshal_with(Tasks)
    def get(self):
        """List all task_id"""
        task_ids = os.listdir(STATIC_FOLDER)
        return { "tasks": task_ids }, 200
            