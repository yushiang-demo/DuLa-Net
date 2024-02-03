from flask_restx import fields
from api.app import api
from .Task import Task

Tasks = api.model('Tasks', {
    'tasks': fields.List(fields.Nested(Task))
})