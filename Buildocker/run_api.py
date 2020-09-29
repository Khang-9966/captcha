import os
import io
import flask
import json
import uuid
import numpy as np 
from flask import Flask
import string
from PIL import Image
import cv2
import base64
import pickle
import tensorflow as tf
import imutils

global label , model
MODEL_FILENAME = 'best_model.h5'
model = tf.keras.models.load_model(MODEL_FILENAME)
label = '0123456789'+string.ascii_uppercase

def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(imgdata))
    image_ = np.array(image)
    image.close()
    return cv2.cvtColor(np.array(image_), cv2.COLOR_BGR2RGB)

def resize_to_fit(image, width, height):
    """
    A helper function to resize an image to fit within a given size
    :param image: image to resize
    :param width: desired width in pixels
    :param height: desired height in pixels
    :return: the resized image
    """

    # grab the dimensions of the image, then initialize
    # the padding values
    (h, w) = image.shape[:2]

    # if the width is greater than the height then resize along
    # the width
    if w > h:
        image = imutils.resize(image, width=width)

    # otherwise, the height is greater than the width so resize
    # along the height
    else:
        image = imutils.resize(image, height=height)

    # determine the padding values for the width and height to
    # obtain the target dimensions
    padW = int((width - image.shape[1]) / 2.0)
    padH = int((height - image.shape[0]) / 2.0)

    # pad the image then apply one more resizing to handle any
    # rounding issues
    image = cv2.copyMakeBorder(image, padH, padH, padW, padW,
        cv2.BORDER_REPLICATE)
    image = cv2.resize(image, (width, height))

    # return the pre-processed image
    return image

def get_captcha(image):
    # Load the image and convert it to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Add some extra padding around the image
    image = cv2.copyMakeBorder(image, 5, 5, 5, 5, cv2.BORDER_REPLICATE)
    
    thres = np.median(image) - 1
    thresh = cv2.threshold(image, thres , 255, cv2.THRESH_BINARY_INV)[1]
    
    # find the contours (continuous blobs of pixels) the image
    contours,_ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   
    letter_image_regions = []
    
    order_x_list = []
    
    for contour in contours:
        # Get the rectangle that contains the contour
        (x, y, w, h) = cv2.boundingRect(contour)

        if w / h > 1.4:
            # This contour is too wide to be a single letter!
            # Split it in half into two letter regions!
            half_width = int(w / 2)
            letter_image_regions.append((x, y, half_width, h))
            letter_image_regions.append((x + half_width, y, half_width, h))
            order_x_list.append(x)
            order_x_list.append(x+half_width)
            continue
        else:
            # This is a normal letter by itself
            letter_image_regions.append((x, y, w, h))
        order_x_list.append(x)
    

    right_order = np.array(order_x_list).argsort()
    letter_image_regions = np.array(letter_image_regions)[right_order]

    # If we found more or less than 4 letters in the captcha, our letter extraction
    # didn't work correcly. Skip the image instead of saving bad training data!
    if len(letter_image_regions) != 4:
        return {"success":False, "captcha": None}

    input_image = image      

    return_string = ""
    for letter_bounding_box in letter_image_regions:
        # Grab the coordinates of the letter in the image
        x, y, w, h = letter_bounding_box
        
        # Extract the letter from the original image with a 2-pixel margin around the edge
        
        y_min = np.clip(y - 2,0,image.shape[0] - 1)
        y_max = np.clip(y + h + 2,0,image.shape[0] - 1)
        x_min = np.clip(x - 2,0,image.shape[1] - 1)
        x_max = np.clip( x + w + 2,0,image.shape[1] - 1)
        
        letter_image = input_image[y_min:y_max, x_min: x_max]
        
        # Re-size the letter image to 20x20 pixels to match training data
        letter_image = resize_to_fit(letter_image, 20, 20)

        # Turn the single image into a 4d list of images to make Keras happy
        letter_image = np.expand_dims(letter_image, axis=2)
        letter_image = np.expand_dims(letter_image, axis=0)
        
        # Ask the neural network to make a prediction
        prediction = model.predict(letter_image)
        
        # Convert the one-hot-encoded prediction back to a normal letter
        letter = label[prediction.argmax()]
        return_string += letter      
    return {"success":True, "captcha": return_string}


app = Flask(__name__)

@app.route("/getcaptcha", methods=['GET'])
def getcaptcha():
    image_base64 =  flask.request.args.get("image")
    if (image_base64 is None):
        image_base64 = flask.request.form.get("image")
    image = stringToRGB( image_base64 )
    #for _ in range(10):
    result = get_captcha(image)
    return flask.jsonify(result)

if __name__ == "__main__":
    app.run(debug=False,port=80,host='0.0.0.0')
    
    
    
