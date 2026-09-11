# Cats vs Dogs Image Classification - Summary

## Project Overview
This project implements a binary image classification model to classify images as either cats or dogs using a Convolutional Neural Network (CNN).

## Dataset
The model was trained using the Microsoft Cats and Dogs dataset. Images were cleaned and divided into training, validation, and test sets. Images were resized to 128×128 pixels and normalized to a range of 0 to 1.

## Model
A CNN was developed using TensorFlow and Keras. The model contains three convolutional layers, max-pooling layers, global average pooling, a dense layer, dropout, and a sigmoid output layer.

## Results
The model was trained for 3 epochs and evaluated on 3,744 clean test images.

- Test Accuracy: 80.61%
- Test Loss: 0.4357
- Cat Precision: 0.84
- Cat Recall: 0.76
- Dog Precision: 0.78
- Dog Recall: 0.85
- Macro F1-score: 0.81

The confusion matrix and sample inference images are included in the `outputs` folder.

## Conclusion
The CNN achieved 80.61% test accuracy and successfully learned to distinguish between cats and dogs. The model can be further improved using data augmentation, additional training epochs, or transfer learning with a pretrained model.