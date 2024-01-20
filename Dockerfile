FROM python:3.10

# ImportError: libGL.so.1
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip

# https://pytorch.org/
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

#RUN pip install matplotlib scikit-image opencv-python pylsd-nova==1.2.0
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python"]