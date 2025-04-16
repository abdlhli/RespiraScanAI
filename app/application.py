from flask import Flask, render_template, request
from keras.preprocessing import image
from keras.models import load_model
from werkzeug.utils import secure_filename
import numpy as np
from PIL import Image
import io
from .model_download import download_model

app = Flask(__name__)

# Load model pada variable global
model = None


def load_ai_model():
    global model
    if model is None:
        model_path = download_model()
        model = load_model(model_path)

# Load model saat startup


@app.before_first_request
def startup():
    load_ai_model()


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
    # Pastikan model sudah diload
    if model is None:
        load_ai_model()

    result = None
    img_path = None
    img_filename = None
    resultwithconfident = None
    percentages = []

    if request.method == 'POST':
        img = request.files['file']

        # Convert FileStorage to PIL Image
        img_data = img.read()
        img_pil = Image.open(io.BytesIO(img_data))

        # Convert RGBA to RGB if necessary
        if img_pil.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img_pil.size, (255, 255, 255))
            background.paste(img_pil, mask=img_pil.split()[-1])
            img_pil = background

        # Save the image
        img_filename = secure_filename(img.filename)
        img_path = "app/static/uploads/" + img_filename
        img_pil.save(img_path)

        # Load and preprocess image for prediction
        img_array = image.img_to_array(img_pil.resize((250, 250)))
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        prediction = model.predict(img_array)

        predicted_class = np.argmax(prediction)
        confidence = np.max(prediction)
        class_labels = ["Corynebacterium diphteriae", "Mycobacterium tuberculosis",
                        "Pharyngitis", "Staphylococcus aureus", "Streptococcus pneumoniae"]
        predicted_label = class_labels[predicted_class]

        # Sort percentages from highest to lowest
        percentages = sorted(list(zip(class_labels, prediction[0])),
                             key=lambda x: x[1],
                             reverse=True)

        result = predicted_label
        resultwithconfident = f"Bakteri {predicted_label}, Dengan Confidence {confidence:.2%}"

    return render_template('mulai.html', result=result, uploaded_image=img_filename,
                           resultwithconfident=resultwithconfident, percentages=percentages)


if __name__ == '__main__':
    app.run(debug=True)
