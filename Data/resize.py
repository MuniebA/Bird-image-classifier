from PIL import Image
import os


def resize_with_padding(image_path, target_size=(224, 224)):
    # Open the image
    image = Image.open(image_path)

    # Calculate the aspect ratio
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height

    # Determine the new size keeping the aspect ratio
    if aspect_ratio > 1:  # Wider than tall
        new_width = target_size[0]
        new_height = int(target_size[0] / aspect_ratio)
    else:  # Taller than wide or square
        new_width = int(target_size[1] * aspect_ratio)
        new_height = target_size[1]

    # Resize the image using LANCZOS resampling
    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Create a new image with the target size and a white background
    new_image = Image.new("RGB", target_size,
                          (255, 255, 255))  # White background

    # Calculate padding
    x_padding = (target_size[0] - new_width) // 2
    y_padding = (target_size[1] - new_height) // 2

    # Paste the resized image onto the new image
    new_image.paste(image, (x_padding, y_padding))

    return new_image


# Example usage
data_dir = 'data/Train'  # Directory with your images
output_dir = 'data/Train_resized'  # Directory to save resized images

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Recursively iterate through all subdirectories
for root, dirs, files in os.walk(data_dir):
    for filename in files:
        # Check for image files by extension
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(root, filename)

            # Get the relative path of the image to preserve folder structure
            relative_path = os.path.relpath(image_path, data_dir)

            # Create the corresponding output subdirectory
            output_subdir = os.path.join(
                output_dir, os.path.dirname(relative_path))
            os.makedirs(output_subdir, exist_ok=True)

            # Resize the image
            resized_image = resize_with_padding(image_path)

            # Save the resized image to the output directory
            output_image_path = os.path.join(output_subdir, filename)
            resized_image.save(output_image_path)

print("Resizing completed and images saved to:", output_dir)
