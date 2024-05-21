# PlantDefend: Potato Disease Classifier

# Introduction

PlantDefend is a cutting-edge web application designed to accurately classify potato diseases, providing farmers and agricultural enthusiasts with a powerful tool for early detection and management. By leveraging deep learning algorithms, PlantDefend aims to enhance crop health and productivity through proactive disease management.

# Features

Disease Classification: Utilizes a pre-trained deep learning model to classify potato leaf images into categories such as Early Blight, Late Blight, or Healthy.

User-friendly Interface: A simple and intuitive web interface for uploading leaf images and receiving instant classification results.

Cross-Platform Compatibility: Accessible via any device with a web browser.

# Technology Stack

Frontend: HTML5, CSS3, JavaScript

Backend: Python, FastAPI

Machine Learning Frameworks: Tensorflow, Keras

Deep Learning Model: CNN

# Setup and Installation

Ensure you have Python 3.8+ and pip installed on your system.

Clone the repository
```sh
git clone https://github.com/yourgithubusername/plantdefend.git
cd plantdefend
```
Install dependencies
```sh
pip install -r requirements.txt
```

Run the application

Start the backend server:

```sh
uvicorn main:app --reload
```

Open index.html or landingpage.html in a web browser for the frontend.

# Usage
Navigate to the web application using your browser.

Upload an image of a potato leaf by clicking the "Select Image" button.

Click the "Predict" button to receive the classification result.

The result will display the disease category along with confidence levels.

# Landing Page
![Image Description](https://github.com/ajafarsadiq2002/Deep-Learning/blob/acc607d6d667cd2b86e81ea58c0e10b5bb723938/PlantDefend-Potato%20Disease%20Classifier/Landing%20Page.jpeg)
# Prediction Page
![Image Description](https://github.com/ajafarsadiq2002/Deep-Learning/blob/52aab9695dac124f66239a75e7ae45de8a1b97e8/PlantDefend-Potato%20Disease%20Classifier/Prediction%20Page.jpeg)
