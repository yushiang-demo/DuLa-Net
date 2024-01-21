import os
import sys
import argparse

from PIL import Image
from flask import Flask, render_template, request
from io import BytesIO
import uuid

from tasks import inference
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return render_template('index.html', error='No selected file')

        # Check if the file is allowed based on the file extension or content type
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        if '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in allowed_extensions:

            storage = './assets/storage/'
            id = str(uuid.uuid4())
            output = os.path.join(storage,id)
            os.makedirs(output)
            
            # Convert the uploaded image to a PIL Image
            pil_image = Image.open(BytesIO(file.read()))
            img_bytes = BytesIO()
            pil_image.save(img_bytes, format='JPEG')
            img_base64 = base64.b64encode(img_bytes.getvalue()).decode()

            inference.delay(img_base64, output)
            
            return render_template('index.html', success=f'File successfully uploaded and processed to {id}')
        else:
            return render_template('index.html', error='Invalid file type. Allowed types: png, jpg, jpeg')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)