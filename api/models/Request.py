from flask_restx import reqparse

class Request():
    def __init__(self):
        self.parser = reqparse.RequestParser(bundle_errors=True)

    def addFile(self, name, required):
        self.parser.add_argument(
            name,
            required=required,
            type=reqparse.FileStorage,
            location='files'
        )