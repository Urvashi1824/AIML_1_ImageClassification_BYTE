# Cats vs Dogs Image Classification 🐱🐶

A binary image classification project using a Convolutional Neural Network (CNN) to classify images as either a Cat or a Dog.

## 🚀 Live Demo

[Try the Live Cats vs Dogs Classifier](https://aiml-1-imageclassification-byte-1.onrender.com/)

## 📌 Project Overview

This project implements a binary image classification system using TensorFlow and Keras.

The model is trained to distinguish between cat and dog images and is also deployed as a web application using Flask and Render.

## 📂 Dataset

The project uses the Microsoft Cats and Dogs dataset.

The images were:

- Cleaned to remove invalid/corrupted images
- Resized to 128 × 128 pixels
- Normalized to values between 0 and 1
- Divided into training, validation, and test sets

## 🧠 Model

A Convolutional Neural Network (CNN) was developed using TensorFlow and Keras.

The model contains:

- 3 Convolutional layers
- Max Pooling layers
- Global Average Pooling
- Dense layer
- Dropout layer
- Sigmoid output layer

## 📊 Results

The model was trained for 3 epochs and evaluated on 3,744 clean test images.

- **Test Accuracy:** 80.61%
- **Test Loss:** 0.4357
- **Macro F1-score:** 0.81

### Classification Performance

| Class | Precision | Recall | F1-score |
|-------|-----------|--------|----------|
| Cat | 0.84 | 0.76 | 0.80 |
| Dog | 0.78 | 0.85 | 0.81 |

## 📈 Confusion Matrix

The confusion matrix is available in:

`outputs/confusion_matrix.png`

## 🖼️ Sample Inference

The project includes 10 sample inference images with predictions:

- `sample_inference_01.png`
- `sample_inference_02.png`
- `sample_inference_03.png`
- `sample_inference_04.png`
- `sample_inference_05.png`
- `sample_inference_06.png`
- `sample_inference_07.png`
- `sample_inference_08.png`
- `sample_inference_09.png`
- `sample_inference_10.png`

## 📁 Project Structure

```text
Cats-vs-Dogs-Classification/
│
├── data/
├── models/
│   └── cats_vs_dogs_model.keras
├── notebooks/
├── outputs/
│   ├── confusion_matrix.png
│   └── sample_inference_01.png - sample_inference_10.png
├── app.py
├── inference.py
├── train.py
├── requirements.txt
├── README.md
└── summary.md
````

## ⚙️ How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Inference

```bash
python inference.py "data/PetImages/Cat/0.jpg"
```

The program will display the predicted class and confidence.

### Example Output

```text
Prediction: Cat
Confidence: 73.29%
```

## 🌐 Web Application

The Flask web application allows users to:

1. Upload a cat or dog image
2. Process the image
3. Predict the class
4. Display the prediction and confidence score

The application is deployed using Render.

## 🔮 Future Improvements

The model can be improved using:

* Data augmentation
* More training epochs
* Transfer learning
* Pre-trained CNN models

## ✅ Conclusion

The CNN successfully learned to classify cats and dogs with **80.61% test accuracy**.

The project includes the trained model, inference script, evaluation metrics, confusion matrix, sample predictions, documentation, and a live web deployment.
