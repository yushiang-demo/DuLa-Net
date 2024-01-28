import os
from flask_restx import Resource

from api.constant import STATIC_FOLDER
from api.app import api

from flask_restx import fields
task_ids_model = api.model('TaskIds', {
    'task_ids': fields.List(fields.String)
})
admin_tasks_response_model = api.model('AdminTasksResponse', {
    'data': fields.Nested(task_ids_model)
})

class Tasks(Resource):
    @api.marshal_with(admin_tasks_response_model)
    def get(self):
        """List all task_id"""
        task_ids = os.listdir(STATIC_FOLDER)
        
        return {
            "data":{
                "task_ids": task_ids
            }
        }, 200