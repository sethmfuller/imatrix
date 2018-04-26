import os
import json
import cv2
import math as m
import pandas as pd
from PIL import Image
import PIL.ImageOps  
from numpy.linalg import inv
from numpy.linalg import det
from numpy.linalg import eig
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.models import load_model
from base64 import b64decode as b64decode
from werkzeug.utils import secure_filename
from flask import Flask, request, redirect, url_for
from keras.preprocessing.image import load_img, img_to_array


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

@app.route("/")
def index():
    return "Send a image as a POST request to localhost:5000/upload"

# Endpoint to send image to server
@app.route("/upload", methods=['POST'])
def uploadImage():
    img64 = request.form['image']
    img64 = img64[22:] # get rid of prefix
    imgDecoded = b64decode(img64)

    with open('output.jpg', 'wb') as f:
        f.write(imgDecoded)

    # Load Image
    filename = 'output.jpg'
    im = load_img(filename, target_size=(56, 56), grayscale=True)
    
    

    # Crop Image
    im_quad2 = im.crop((28, 0, 56, 28))

    im_quad2.save("im_quad2.jpg")

    im_quad1 = im.crop((0, 0, 28, 28))

    im_quad1.save("im_quad1.jpg")

    im_quad3 = im.crop((0, 28, 28, 56))

    im_quad3.save("im_quad3.jpg")

    im_quad4 = im.crop((28, 28, 56, 56))

    im_quad4.save("im_quad4.jpg")


    # Preprocess each sub-image
    im_quad1 = img_to_array(im_quad1)
    im_quad1 = 255 - im_quad1
    im_quad1 /= 255
    im_quad1 = im_quad1.reshape(-1,28,28,1)

    im_quad2 = img_to_array(im_quad2)
    im_quad2 = 255 - im_quad2
    im_quad2 /= 255
    im_quad2 = im_quad2.reshape(-1, 28,28,1)

    im_quad3 = img_to_array(im_quad3)
    im_quad3 = 255 - im_quad3
    im_quad3 /= 255
    im_quad3 = im_quad3.reshape(-1, 28,28,1)

    im_quad4 = img_to_array(im_quad4)
    im_quad4 = 255 - im_quad4
    im_quad4 /= 255
    im_quad4 = im_quad4.reshape(-1, 28,28,1)

    # Load Model
    model = load_model("Mohler_Model.h5")

    # Predict each image
    im_quad1_prediction = int(model.predict_classes(im_quad1)[0])
    print(model.predict_classes(im_quad1))
    im_quad2_prediction = int(model.predict_classes(im_quad2)[0])
    print(model.predict_classes(im_quad2))
    im_quad3_prediction = int(model.predict_classes(im_quad3)[0])
    print(model.predict_classes(im_quad3))
    im_quad4_prediction = int(model.predict_classes(im_quad4)[0])
    print(model.predict_classes(im_quad4))

    # Calculations

    # matrix A
    a = np.matrix([[im_quad1_prediction, im_quad2_prediction], [im_quad3_prediction, im_quad4_prediction]])

    # compute determinant
    a_det = det(a)

    # compute inverse
    a_inv = inv(a)

    row1_1 = float(a_inv[:,0][0])
    row1_2 = float(a_inv[:,1][0])
    row2_1 = float(a_inv[:,0][1])
    row2_2 = float(a_inv[:,1][1])



    # Dummy Data
    result = {
        "determinant": a_det,
        "inverse": [[row1_1, row1_2], [row2_1, row2_2]],
        "values": [[im_quad1_prediction, im_quad2_prediction], [im_quad3_prediction, im_quad4_prediction]],
    }
    result = json.dumps(result)
    


    return  (result, 200, {'Access-Control-Allow-Origin': '*'})
 
