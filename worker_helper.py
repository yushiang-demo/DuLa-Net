import os
import io
import base64
from PIL import Image
from celery import Celery

BROKER_URL = os.environ.get('BROKER_URL')
BACKEND_URL = os.environ.get('BACKEND_URL')
APP_NAME = os.environ.get('APP_NAME')
TASK_NAME = os.environ.get('TASK_NAME')
CALLBACK_URL = os.environ.get('CALLBACK_URL')
app = Celery(APP_NAME, broker=BROKER_URL, backend=BACKEND_URL)

def inference_from_file(file, output, id, callback_url=CALLBACK_URL):
    pil_image = Image.open(io.BytesIO(file.read()))
    img_bytes = io.BytesIO()
    pil_image.save(img_bytes, format='JPEG')
    img_base64 = base64.b64encode(img_bytes.getvalue()).decode()
    app.send_task(TASK_NAME, args=[img_base64, output, id, callback_url])