import os
import uuid
from tasks import inferenceFromFile
from api.constant import STATIC_FOLDER

from api.app import api

from flask_restx import Resource

from flask_restx import fields, reqparse

upload_data_model = api.model('UploadData', {
    'uuid': fields.String(description='Uploaded uuid')
})
upload_response_model = api.model('UploadResponse', {
    'data': fields.Nested(upload_data_model , description='Data container for upload response')
})

upload_parser = reqparse.RequestParser(bundle_errors=True)
upload_parser.add_argument(
    'file',
    required=True,
    type=reqparse.FileStorage,
    location='files'
)

class Task(Resource):
    @api.expect(upload_parser)
    @api.marshal_with(upload_response_model)
    def post(self):
        """Create a task"""
        args = upload_parser.parse_args()
        file = args.file

        if file:

            id = str(uuid.uuid4())      
            output = os.path.join(STATIC_FOLDER, id)
            os.makedirs(output)
            inferenceFromFile(file, output)
            return { 'data': {'uuid': id}}, 201
        else:
            return {}, 400