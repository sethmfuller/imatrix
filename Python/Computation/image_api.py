import os
import json
from numpy import *
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

# endpoint to send image to server
@app.route("/upload", methods=['POST'])
def uploadImage():
    img64 = request.form['image']
    img64 = img64[22:] # get rid of prefix
    imgDecoded = b64decode(img64)

    with open('output.jpg', 'wb') as f:
        f.write(imgDecoded)

    # Load Image
    im = load_img('output.jpg', target_size=(28,28), grayscale=True)

    # Splice up image
    #im_quad1 = im.crop((125, 25, 180, 100))
    #im_quad2 = im.crop((25, 25, 100, 100))
    #im_quad3 = im.crop((30, 125, 100, 200))
    #im_quad4 = im.crop((115, 115, 180, 224))

    # Preprocess each sub-image
    im_quad1 = img_to_array(im)
    im_quad1 = 255 - im_quad1
    im_quad1 /= 255
    im_quad1 = im_quad1.reshape(-1, 28,28,1)

    im_quad2 = img_to_array(im)
    im_quad2 = 255 - im_quad2
    im_quad2 /= 255
    im_quad2 = im_quad2.reshape(-1, 28,28,1)

    im_quad3 = img_to_array(im)
    im_quad3 = 255 - im_quad3
    im_quad3 /= 255
    im_quad3 = im_quad3.reshape(-1, 28,28,1)

    im_quad4 = img_to_array(im)
    im_quad4 = 255 - im_quad4
    im_quad4 /= 255
    im_quad4 = im_quad4.reshape(-1, 28,28,1)

    # Load pretrained neural network model
    model = load_model("matrix_model.h5")

    # Predict each image
    quad1_prediction = model.predict_classes(im_quad1)[0]
    quad2_prediction = model.predict_classes(im_quad2)[0]
    quad3_prediction = model.predict_classes(im_quad3)[0]
    quad4_prediction = model.predict_classes(im_quad4)[0]    

    # Calculations
    
    

    # Dummy Data
    result = {
        "determinant": 54,
        "inverse": [[1,0],[3,4]],
        "values": [[int(quad2_prediction), int(quad1_prediction)],[int(quad3_prediction), int(quad4_prediction)]],
    }
    result = json.dumps(result)
    


    return  (result, 200, {'Access-Control-Allow-Origin': '*'})
 
