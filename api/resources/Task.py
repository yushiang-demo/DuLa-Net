import os
import uuid
from tasks import inferenceFromFile
from api.constant import STATIC_FOLDER

from api.app import api

from flask import request
from flask_restx import Resource
from api.models import Request, Task

input = Request()
input.addFile(name='file',required=True)


class Task(Resource):
    @api.expect(input.parser)
    @api.marshal_with(Task)
    def post(self):
        """Create a task"""
        args = input.parser.parse_args()
        file = args.file
        if file:

            id = str(uuid.uuid4())      
            output = os.path.join(STATIC_FOLDER, id)
            os.makedirs(output)
            inferenceFromFile(file, output)
    
            output = {
                'uuid': id,
                'images':{
                    'origin': f"http://localhost/files/storage/{id}/image.jpg",
                    'preview': f"http://localhost/files/storage/{id}/vis.jpg",
                    'aligned': f"http://localhost/files/storage/{id}/raw.jpg",
                }
            }
            return output, 200
        else:
            return {}, 400