from flask_restx import fields
from api.app import api

Layout = api.model('Layout',{
    'data': fields.Raw,
})

Images = api.model('Images',{
    'preview': fields.String,
    'origin': fields.String,
    'aligned': fields.String,
})

Task = api.model('Task', {
    'uuid':  fields.String,
    'images': fields.Nested(Images),
    'layout': fields.Nested(Layout),
})