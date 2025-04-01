from flask import Flask, render_template, request
from keras.preprocessing import image
from keras.models import load_model
from werkzeug.utils import secure_filename
import numpy as np

app = Flask(__name__)
model = load_model('app/model/model_bakteri_inception_resnet_v2.keras')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/obyek')
def obyek():
    return render_template('obyek.html')


@app.route('/metode')
def metode():
    return render_template('metode.html')


@app.route('/arsitektur')
def arsitektur():
    return render_template('arsitektur.html')


@app.route('/kreator')
def kreator():
    return render_template('kreator.html')


@app.route('/mulai', methods=['GET', 'POST'])
def mulai():
    result = None
    img_path = None
    img_filename = None
    resultwithconfident = None

    if request.method == 'POST':
        img = request.files['file']
        img_filename = secure_filename(img.filename)
        img_path = "app/static/uploads/" + img_filename
        img.save(img_path)

        img = image.load_img(img_path, target_size=(250, 250))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        prediction = model.predict(img_array)

        predicted_class = np.argmax(prediction)
        confidence = np.max(prediction)
        class_labels = ["Corynebacterium Diphteriae", "Mycobacterium Tuberculosis",
                        "Neisseria Gonorroeae", "Staphylococcus Aureus", "Streptococcus Pneumoniae"]
        predicted_label = class_labels[predicted_class]

        result = predicted_label
        resultwithconfident = f"Bakteri {predicted_label}, Dengan Confidence {confidence:.2%}"

    return render_template('mulai.html', result=result, uploaded_image=img_filename, resultwithconfident=resultwithconfident)


if __name__ == '__main__':
    app.run(debug=True)
