from rembg import remove
from PIL import Image, ImageEnhance

def change_image_color(input_path, color, output_path):
    # Open the input image and remove the background
    input_image = Image.open(input_path)
    input_image_no_bg = remove(input_image)
    
    # Create a new image with the same size and the specified color
    color_image = Image.new("RGBA", input_image_no_bg.size, color)
    
    # Combine the color image with the input image
    combined_image = Image.alpha_composite(color_image, input_image_no_bg)
    
    # Save the output image
    combined_image.save(output_path, format='PNG')
    
    print("Image color change complete. The output image is saved at:", output_path)

# Paths to input and output images
input_path = 'download.jpg'
output_path = 'output_with_new_color.png'
color = (255, 0, 0, 255)  # Red color in RGBA

# Change the image color
change_image_color(input_path, color, output_path)



