"""
complex_assignment_45:

Write a Python Program to join two pictures.

"""
from PIL import Image



from PIL import Image

def join_pictures_horizontally(image1_path, image2_path, output_path):
    # Open the first image
    image1 = Image.open(image1_path)

    # Open the second image
    image2 = Image.open(image2_path)

    # Calculate the width of the final joined image
    new_width = image1.width + image2.width

    # Calculate the maximum height of the two images
    new_height = max(image1.height, image2.height)

    # Create a new image with the calculated dimensions
    new_image = Image.new('RGB', (new_width, new_height))

    # Paste the first image on the left side of the new image
    new_image.paste(image1, (0, 0))

    # Paste the second image on the right side of the new image
    new_image.paste(image2, (image1.width, 0))

    # Save the joined image
    new_image.save(output_path)

    print("Images joined successfully!")


# Example usage
image1_path = 'E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem45/image.png'  # Replace with the path to your first image
image2_path = 'E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem45/img1.png'  # Replace with the path to your second image
output_path = 'E:/bulding/python_exercises/3-Advanced/Study Matrials Complex Problem45/img2.png'  # Replace with the desired output path

join_pictures_horizontally(image1_path, image2_path, output_path)