
# from PIL import Image

# # Open an image file
# img = Image.open('image.jpg')


# # Define the desired dimensions (new width and height)
# new_width = img.width * 2  # Example: doubling the width
# new_height = img.height * 2  # Example: doubling the height

# # Resize the image
# resized_img = img.resize((new_width, new_height), Image.BICUBIC)

# # Save the resized image
# resized_img.save('upscaled_image.jpg')


import tensorflow as tf
import numpy as np
import cv2

# Load the pre-trained EDSR model
model = tf.keras.models.load_model('path_to_pretrained_edsr_model.h5')

# Load and preprocess the image
image = cv2.imread('image.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = np.expand_dims(image, axis=0) / 255.0

# Super-resolve the image
enhanced_image = model.predict(image)
enhanced_image = np.squeeze(enhanced_image, axis=0)
enhanced_image = np.clip(enhanced_image * 255.0, 0, 255).astype(np.uint8)

# Save the enhanced image
cv2.imwrite('enhanced_image.jpg', cv2.cvtColor(enhanced_image, cv2.COLOR_RGB2BGR))
