import io
import numpy as np
import tensorflow as tf
from PIL import Image
from flask import Flask, jsonify, request, render_template, Response
import json
from matplotlib.figure import Figure
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as VirtualCanvas


model = tf.keras.models.load_model('model4_retinal-oct.h5')

def prepare_image(img):
    img = Image.open(io.BytesIO(img))
    img = img.resize((150, 150))
    img = np.expand_dims(img, 0)
    img = np.stack((img,)*3, axis=-1)
    
    return img


def predict_result(img):
    Y_pred = model.predict(img)
    print('Prédiction du modèle: ', Y_pred)
    return np.argmax(Y_pred, axis=1)
#argmax permet de trouver la valeur maximale donc la meilleure prédiction possible de la bonne pathologie

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def infer_image():
    if 'file' not in request.files:
        return "Veuillez réessayer. L'image n'existe pas"
    
    file = request.files.get('file')

    if not file:
        return

    img_bytes = file.read()
    img = prepare_image(img_bytes)
    return jsonify(prediction=int(predict_result(img)))
    


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/chart', methods=['GET'])
def chart():
    param = json.loads(request.args.get("param"))
    print(param)
    
    labels = []
    values =[]
    
    for key in param["datas"]:
        labels.append(key)
        values.append(param["datas"][key])
    #print(labels)
    #print(values)
    
    fig = Figure()
    ax1 = fig.subplots(1, 1)
    ax1.bar(labels, values)
    #fig.savefig("test.png", format="png") 
    
    output = BytesIO()
    VirtualCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')