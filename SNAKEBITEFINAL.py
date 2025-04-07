import numpy as np
import time
import tensorflow.keras
from PIL import Image, ImageOps

start_time = time.time()

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

# Create numpy array to hold the image data
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

"""
Image 1 is a body part image so output should be Other.
Image 2 is a snakebite image but the snake is non venomous.
Image 3 is a snakebite image with venomous snake.
"""

# Load and preprocess the image
image = Image.open('testing/Image1.jpg')
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)  # Fixed the ANTIALIAS issue

# Convert image to numpy array
image_array = np.asarray(image)

# Normalize the image (scaling pixel values to between -1 and 1)
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Run the inference
prediction = model.predict(data)

# Interpret the prediction
if prediction[0][0] > 0.5:  # Changed threshold to 0.5 for better confidence
    print("Match is found.")
    print("Snake bite detected! Snake is venomous.")
elif prediction[0][1] > 0.5:
    print("Match is found.")
    print("Snake bite detected! Snake is non-venomous.")
else:
    print("Snake bite not detected.")

end_time = time.time()
elapsed = end_time - start_time
print(f"Execution time: {elapsed:.2f}s")