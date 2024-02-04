FROM python:3.10

# ImportError: libGL.so.1
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip

#RUN pip install torch torchvision torchaudio matplotlib scikit-image opencv-python pylsd-nova==1.2.0 Celery redis Flask Flask-RESTx pymongo flower
RUN pip install --no-cache-dir -r requirements.txt