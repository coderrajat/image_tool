from rembg import remove
from PIL import Image

def convert_to_black_and_white(input_path, output_path):
    # Open the input image and remove the background
    input_image = Image.open(input_path)
    input_image_no_bg = remove(input_image)
    
    # Convert the image to grayscale (black and white)
    bw_image = input_image_no_bg.convert('L')
    
    # Save the output image
    bw_image.save(output_path, format='PNG')
    
    print("Image converted to black and white. The output image is saved at:", output_path)

# Paths to input and output images
input_path = 'download.jpg'
output_path = 'output_bw.jpg'

# Convert the image to black and white
convert_to_black_and_white(input_path, output_path)
