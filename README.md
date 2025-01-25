# Bird Species Image Classification Using EfficientNet and DINOv2

This repository contains the implementation of a multiclass image classification project for bird species using **EfficientNet** and **DINOv2 Vision Transformer**. The project leverages transfer learning and fine-tuning techniques to classify 200 bird species accurately.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Model Architectures](#model-architectures)
  - [EfficientNet](#efficientnet)
  - [DINOv2 Vision Transformer](#dinov2-vision-transformer)
- [Usage Instructions](#usage-instructions)
- [Results](#results)
- [References](#references)

---

## Project Overview

This project explores two cutting-edge deep learning architectures for image classification tasks:
- **EfficientNet**: A convolutional neural network optimized for speed and accuracy.
- **DINOv2 Vision Transformer**: A self-attention-based model that excels in learning complex patterns.

Both models are fine-tuned on a dataset of 200 bird species with strategies to reduce overfitting, including data augmentation and regularization.

---

## Dataset

- **Dataset Features**:
  - 200 unique bird species.
  - Images resized to **224x224 pixels** for model compatibility.
- **Data Splits**:
  - Training set
  - Testing set
- **Data Augmentation** (EfficientNet only):
  - RandomRotation (15%)
  - RandomFlip (horizontal and vertical)

---

## Model Architectures

### EfficientNet
- **Features**:
  - Depthwise separable convolutions for efficiency.
  - Squeeze-and-Excitation blocks.
  - Dropout rate: 0.2.
- **Hyperparameters**:
  - Learning rate: `0.0001`
  - Batch size: `16` (iteration 1), `32` (iteration 2)
  - Epochs: `30` (iteration 1), `20` (iteration 2)
- **Output**: Softmax activation for class probabilities.

### DINOv2 Vision Transformer
- **Features**:
  - Patch embedding with 384-dimensional representations.
  - Multi-head self-attention.
  - Residual connections and layer normalization.
- **Hyperparameters**:
  - Learning rate adjustment for fine-tuning.
  - Classifier: SVM with L2 regularization.

---

## Usage Instructions

### Prerequisites
Make sure you have the following installed:
- Python 3.8 or above
- TensorFlow 2.x
- PyTorch
- scikit-learn
- Other dependencies listed in the `requirements.txt` file.

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```
2. Extract the dataset into the `Data/` directory.
3. Run the models:
   - **EfficientNet**:
     ```bash
     python model/effinet/2/AML_efficientnet.ipynb
     ```
   - **DINOv2**:
     ```bash
     python model/dinvo-Transformare/1/Dinov2_Image_Classifier.ipynb
     ```

4. Evaluate the models using the test set.

---

## Results

| Model         | Iteration | Top-1 Accuracy (%) | Top-5 Accuracy (%) |
|---------------|-----------|---------------------|---------------------|
| EfficientNet  | 1         | xx.xx              | xx.xx              |
| DINOv2        | 1         | xx.xx              | xx.xx              |

Detailed analysis and results can be found in the `report/` folder.

---

## References
- **EfficientNet**: https://arxiv.org/abs/1905.11946
- **DINOv2 Vision Transformer**: https://arxiv.org/abs/2304.07193
- Dataset: Your dataset source (if public).

---
