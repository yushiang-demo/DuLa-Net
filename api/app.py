from flask import Flask, send_from_directory, jsonify
from flask_restx import Api
from mongodb.app import db

app = Flask(__name__)
app.config['RESTX_MASK_SWAGGER'] = False
api = Api(app, version='1.0', title='DuLa-Net APIs', prefix='/api', base_url='/api')

import traceback
# Global error handler for all other exceptions
@app.errorhandler(Exception)
def handle_unexpected_error(error):
    # Log the error for debugging purposes
    app.logger.error('Unhandled Exception: %s', traceback.format_exc())
    
    # Return a generic error response
    return {'message': 'An unexpected error occurred'}, 500


@app.errorhandler(400)
def handle_bad_request(error):
    return {'message': 'Bad Request', 'error': str(error)}, 400