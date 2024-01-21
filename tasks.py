import io
import os
import sys
import argparse

import numpy as np
from PIL import Image

import torch
from torch.autograd import Variable
from torchvision import transforms

import Layout
import Utils

import config as cf
from Model import DuLaNet, E2P

import postproc

from Preprocess.pano_lsd_align import panoEdgeDetection, rotatePanorama

import base64

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def preprocess(img, q_error=0.7, refine_iter=3):
    img_ori = np.array(img.resize((1024, 512),  Image.Resampling.BICUBIC))[..., :3]

    # VP detection and line segment extraction
    _, vp, _, _, panoEdge, _, _ = panoEdgeDetection(img_ori,
                                                    qError=q_error,
                                                    refineIter=refine_iter)
    panoEdge = (panoEdge > 0)

    # Align images with VP
    i_img = rotatePanorama(img_ori / 255.0, vp[2::-1])

    return Image.fromarray(np.uint8(i_img * 255.0))

def predict(model, img):
    model.eval()

    trans = transforms.Compose([
            transforms.Resize((cf.pano_size)),
            transforms.ToTensor()
        ])
    color = torch.unsqueeze(trans(img), 0).to(device)

    [fp, fc, h] = model(color)

    e2p = E2P(cf.pano_size, cf.fp_size, cf.fp_fov)
    [fc_up, fc_down] = e2p(fc)

    [fp, fc_up, fc_down, h] = Utils.var2np([fp, fc_up, fc_down, h])
    fp_pts, fp_pred = postproc.run(fp, fc_up, fc_down, h)

    # Visualization 
    scene_pred = Layout.pts2scene(fp_pts, h)
    edge = Layout.genLayoutEdgeMap(scene_pred, [512 , 1024, 3], dilat=2, blur=0)

    img = img.resize((1024,512))
    img = np.array(img, float) / 255
    vis = img * 0.5 + edge * 0.5

    vis = Image.fromarray(np.uint8(vis* 255))
    return vis, scene_pred

from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/0'
app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL)

@app.task
def inference(image_data_base64, output, seed=224, backbone='resnet18',ckpt = './Model/ckpt/res18_realtor.pkl'):

    # initialize DuLa-net
    np.random.seed(seed)
    torch.manual_seed(seed)

    model = DuLaNet(backbone).to(device)

    #model.load_state_dict(torch.load(args.ckpt))
    model.load_state_dict(torch.load(ckpt, map_location=str(device)))

    image_data = base64.b64decode(image_data_base64)
    pil_image = Image.open(io.BytesIO(image_data))
    img = preprocess(pil_image)
    vis, scene_pred = predict(model, img)
    
    pil_image.save(os.path.join(output,"raw.jpg"))
    img.save(os.path.join(output,"image.jpg"))
    vis.save(os.path.join(output,"vis.jpg"))
    Layout.saveSceneAsJson(os.path.join(output,"layout.json"), scene_pred)
    return output