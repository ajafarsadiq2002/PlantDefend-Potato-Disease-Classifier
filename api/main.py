from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

# Adjust CORS settings as necessary
origins = ["*"]  # List of origins that should be allowed to make requests to the API

app.add_middleware(     
    CORSMiddleware,     
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model(r"C:\Users\JAFAR\Downloads\PROJECTS\DEEP LEARNING PROJECTS\PlantDefend-Potato Disease Classifier FullStack\potato_disease_model.h5")

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

def read_file_as_image(data) -> np.ndarray:     # Function to read the image file as numpy array 
    image = Image.open(BytesIO(data))
    image = image.resize((256, 256))  # Adjust the size as per your model's requirement
    return np.array(image)

@app.post("/predict/")
async def predict(  # http://localhost:8000/predict
    file: UploadFile = File(...) 
):
    image = read_file_as_image(await file.read()) # Read the uploaded image file as numpy array
    img_batch = np.expand_dims(image, axis= 0)         # Add a batch dimension to the image
    
    predictions = MODEL.predict(img_batch)      # Get the model's prediction

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])] # Get the class name with the highest confidence
    confidence = np.max(predictions[0])                     # Get the confidence of the prediction
    return {
        'class': predicted_class,   # Return the predicted class and confidence
        'confidence': float(confidence) 
    }

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)