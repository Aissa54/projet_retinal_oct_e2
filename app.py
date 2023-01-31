import io
from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
from PIL import Image
import logging

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

logging.basicConfig(level=logging.DEBUG)
model = tf.keras.models.load_model('model4_retinal-oct.h5')

classes = ['CNV', 'DME', 'DRUSEN', 'NORMAL']

def prepare_image(img):
    """
    prepares the image for the api call
    """
    img = Image.open(io.BytesIO(img)).convert('RGB')
    img = img.resize((150, 150))
    img = np.array(img)
    img = np.expand_dims(img, 0)
    return img

def predict_result(img):
    """predicts the result"""
    return np.argmax(model.predict(img)[0])

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def infer_image():
    if 'file' not in request.files:
        return "Please try again. The Image doesn't exist"
    file = request.files.get('file')
    if not file:
        return
    img_bytes = file.read()
    img = prepare_image(img_bytes)
    predictions = model.predict(img)[0].tolist()
    prediction = np.argmax(predictions)
    
    # Mapping prediction to class
    class_mapping = {0: 'CNV', 1: 'DME', 2: 'DRUSEN', 3: 'NORMAL'}
    prediction_class = class_mapping.get(prediction, "Unknown")
    
    return render_template('predict.html', prediction=prediction_class, class_probabilities=predictions)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', use_reloader=False)
