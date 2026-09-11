import os

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["TF_NUM_INTRAOP_THREADS"] = "1"
os.environ["TF_NUM_INTEROP_THREADS"] = "1"
from flask import Flask, request, render_template_string
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

app = Flask(__name__)

MODEL_PATH = "models/cats_vs_dogs_model.keras"
IMG_SIZE = 128

model = load_model(MODEL_PATH)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Cats vs Dogs Classifier</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background: #f4f4f4;
        }
        .box {
            background: white;
            padding: 35px;
            max-width: 550px;
            margin: auto;
            border-radius: 15px;
        }
        h1 {
            margin-bottom: 10px;
        }
        input {
            margin: 20px;
        }
        button {
            padding: 12px 25px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        .result {
            margin-top: 25px;
            font-size: 22px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>🐱 Cats vs Dogs 🐶</h1>
        <p>Upload an image to classify it.</p>

        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="image" accept="image/*" required>
            <br>
            <button type="submit">Predict</button>
        </form>

        {% if prediction %}
            <div class="result">
                Prediction: {{ prediction }}<br>
                Confidence: {{ confidence }}
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    confidence = None

    if request.method == "POST":
        file = request.files["image"]

        image = Image.open(file).convert("RGB")
        image = image.resize((IMG_SIZE, IMG_SIZE))

        image_array = np.array(image, dtype=np.float32) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        probability = model.predict(image_array, verbose=0)[0][0]

        if probability >= 0.5:
            prediction = "Dog 🐶"
            confidence = f"{probability:.2%}"
        else:
            prediction = "Cat 🐱"
            confidence = f"{1 - probability:.2%}"

    return render_template_string(
        HTML,
        prediction=prediction,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)