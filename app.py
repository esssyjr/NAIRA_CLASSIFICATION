import gradio as gr
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
import pickle
import cv2
from gtts import gTTS
import os

# Load your model from a pickle file
with open('NAIRA.pkl', 'rb') as file:
    model = pickle.load(file)

# Define class labels
class_labels = ["10", "100", "1000", "20", "200", "5", "50", "500"]

# Define a function for preprocessing the image
def preprocess_image(image):
    image = np.array(image)
    image = cv2.resize(image, (224, 224))  # resize image to the expected input size for your model
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image.astype('float32') / 255.0  # normalize the image
    return image

# Define a function for making predictions and converting text to speech
def predict(image):
    preprocessed_image = preprocess_image(image)
    prediction = model.predict(preprocessed_image)
    predicted_index = np.argmax(prediction, axis=1)[0]
    predicted_class = class_labels[predicted_index]
    prediction_text = f"Predicted class: {predicted_class} NAIRA"
    
    # Convert the prediction text to speech
    tts = gTTS(text=prediction_text, lang='en')
    audio_file = "prediction.mp3"
    tts.save(audio_file)
    
    return prediction_text, audio_file

# Create a Gradio interface
interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(),
    outputs=[gr.Textbox(), gr.Audio(type="filepath")]
)

# Launch the interface
interface.launch(share=True)
