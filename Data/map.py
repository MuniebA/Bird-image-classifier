import os
import re

# Path to the train.txt file
train_txt_path = 'train.txt'
# Path to the output file where the class map will be saved
output_file = 'class_map_clean.txt'

# Dictionary to store class label mappings
class_map = {}

# Regular expression to remove numbers at the end


def clean_bird_name(bird_name):
    return re.sub(r'_\d+$', '', bird_name)


# Read the train.txt file
with open(train_txt_path, 'r') as f:
    for line in f:
        # Split the line to get the bird species and the numeric label
        image_name, class_label = line.strip().split()
        class_label = int(class_label)

        # Extract the bird species name and clean it
        bird_name = '_'.join(image_name.split('_')[:-1])
        bird_name = clean_bird_name(bird_name)

        # Add the bird name and class label to the dictionary if not already present
        if class_label not in class_map:
            class_map[class_label] = bird_name

# Save the cleaned class map to a new text file
with open(output_file, 'w') as f_out:
    for label, bird_name in class_map.items():
        f_out.write(f"{label}: {bird_name}\n")

print(f"Cleaned class map has been saved to {output_file}")
