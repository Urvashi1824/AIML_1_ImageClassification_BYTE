import sys
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

IMG_SIZE = 128
MODEL_PATH = "models/cats_vs_dogs_model.keras"


def predict_image(image_path):
    model = load_model(MODEL_PATH)

    image = Image.open(image_path).convert("RGB")
    image = image.resize((IMG_SIZE, IMG_SIZE))

    image_array = np.array(image, dtype=np.float32) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    probability = model.predict(image_array, verbose=0)[0][0]

    if probability >= 0.5:
        prediction = "Dog"
        confidence = probability
    else:
        prediction = "Cat"
        confidence = 1 - probability

    print(f"Prediction: {prediction}")
    print(f"Confidence: {confidence:.2%}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python inference.py <image_path>")
    else:
        predict_image(sys.argv[1])