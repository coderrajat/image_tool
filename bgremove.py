from rembg import remove
from PIL import Image

# Load the image
input_path = 'bird.webp'
output_path = 'image1.png'

# Open the input image
input_image = Image.open(input_path)

# Remove the background
output_image = remove(input_image)

# Save the output image
output_image.save(output_path)

print("Background removal complete. The output image is saved at:", output_path)
