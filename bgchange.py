from rembg import remove
from PIL import Image

def change_background(input_path, background_path, output_path):
    # Open the input image and remove the background
    input_image = Image.open(input_path)
    input_image_no_bg = remove(input_image)
    
    # Open the new background image
    background_image = Image.open(background_path)
    
    # Resize the background to match the input image size
    background_image = background_image.resize(input_image.size)
    
    # Create a new image by combining the input image without background and the new background
    combined_image = Image.alpha_composite(background_image.convert('RGBA'), input_image_no_bg)
    
    # Save the output image
    combined_image.save(output_path, format='PNG')
    
    print("Background change complete. The output image is saved at:", output_path)

# Paths to input, background, and output images
input_path = 'download.jpg'
background_path = 'background.jpg'
output_path = 'output_with_new_background.png'

# Change the background
change_background(input_path, background_path, output_path)



def change_background(input_path, background_path, output_path):
    # Open the input image and remove the background
    input_image = Image.open(input_path)
    input_image_no_bg = remove(input_image)
    
    # Open the new background image
    background_image = Image.open(background_path)
    
    # Resize the background to match the input image size
    background_image = background_image.resize(input_image.size)
    
    # Create a new image by combining the input image without background and the new background
    combined_image = Image.alpha_composite(background_image.convert('RGBA'), input_image_no_bg)
    
    # Save the output image
    combined_image.save(output_path, format='PNG')
    
    print("Background change complete. The output image is saved at:", output_path)

# Paths to input, background, and output images
input_path = 'input.png'
background_path = 'background.png'
output_path = 'output_with_new_background.png'

# Change the background
change_background(input_path, background_path, output_path)
