from flask_restx import fields
from api.app import api

layoutPoint = api.model('LayoutPoint',{
    'id': fields.Integer,
    'coord': fields.List(fields.Float),
    'xyz': fields.List(fields.Float),
})

layoutPoints = api.model('LayoutPoints', {
    'num': fields.Integer,
    'points': fields.List(fields.Nested(layoutPoint))
})

Layout = api.model('Layout',{
    'cameraHeight': fields.Float,
    'layoutHeight': fields.Float,
    'layoutPoints': fields.Nested(layoutPoints),
})

Images = api.model('Images',{
    'preview': fields.String,
    'origin': fields.String,
    'aligned': fields.String,
})

Task = api.model('Task', {
    'uuid':  fields.String(attribute='_id'),
    'status': fields.String,
    'images': fields.Nested(Images),
    'layout': fields.Nested(Layout),
})