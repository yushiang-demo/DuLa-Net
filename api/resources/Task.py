import os
import uuid
from tasks import inference_from_file
from api.constant import STATIC_FOLDER

from api.app import api, db

from flask import request, jsonify
from flask_restx import Resource, abort
from api.models import Request, Task

postReq = Request()
postReq.addFile(name='file',required=True)

putReq = Request()
putReq.addFile(name='file',required=True)
putReq.addString(name="id",required=True)

getReq = Request()
getReq.addString(name="id",required=True)

delReq = Request()
delReq.addString(name="id",required=True)

class Task(Resource):

    @api.expect(delReq.parser)
    @api.marshal_with(Task)
    def delete(self):
        return None

    @api.expect(getReq.parser)
    @api.marshal_with(Task, code=200)
    def get(self):
        args = getReq.parser.parse_args()
        id = args.id
        task = db.getTask(id)
        if task:
            return task, 200
        else:
            abort(400, message=f'Task {id} not found')

    @api.expect(putReq.parser)
    @api.marshal_with(Task)
    def put(self):
        return None

    @api.expect(postReq.parser)
    @api.marshal_with(Task)
    def post(self):
        args = postReq.parser.parse_args()
        file = args.file
        if file:
            id = db.createTask(f"{request.referrer}files/storage")
            output = os.path.join(STATIC_FOLDER, id)
            os.makedirs(output)
            inference_from_file(file, output, id)

            output = {
                '_id': id
            }
            return output, 200
        else:
            return {}, 400