# Cats vs Dogs Image Classification

## Project Overview
This project is a binary image classification system that uses a Convolutional Neural Network (CNN) to classify images as either a Cat or a Dog.

## Dataset
The project uses the Microsoft Cats and Dogs dataset.

The images were:
- Cleaned to remove invalid/corrupted images
- Resized to 128 × 128 pixels
- Normalized to values between 0 and 1
- Divided into training, validation, and test sets

## Model
A CNN model was built using TensorFlow and Keras.

The model contains:
- 3 Convolutional layers
- Max Pooling layers
- Global Average Pooling
- Dense layer
- Dropout layer
- Sigmoid output layer

## Results

The model was trained for 3 epochs.

- Test Images: 3,744
- Test Accuracy: 80.61%
- Test Loss: 0.4357
- Macro F1-score: 0.81

### Classification Performance

| Class | Precision | Recall | F1-score |
|------|-----------|--------|----------|
| Cat | 0.84 | 0.76 | 0.80 |
| Dog | 0.78 | 0.85 | 0.81 |

## Project Structure

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
├── inference.py
├── train.py
├── requirements.txt
├── README.md
└── summary.md


How to Run :

1. Install dependencies
pip install -r requirements.txt

2. Run inference :

python inference.py "data/PetImages/Cat/0.jpg"

The program will display the predicted class and confidence.


Example Output :

Prediction: Cat
Confidence: 73.29%
Future Improvements


The model can be improved using:

Data augmentation
More training epochs
Transfer learning
Pre-trained CNN models


Conclusion :

The CNN successfully learned to classify cats and dogs with 80.61% test accuracy. The project includes the trained model, inference script, confusion matrix, sample predictions, and documentation.
