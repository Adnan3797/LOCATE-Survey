import os
import shutil

# Define your folder paths
images_folder = "./images"
labels_folder = "./../labelTxt/labelTxt/DOTA-v1.5_train/"
output_folder = "./labels/"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get a set of image file names without extensions from the images folder
image_names = {
    os.path.splitext(file)[0]
    for file in os.listdir(images_folder)
    if file.endswith(".png")
}

# Process label files
for label_file in os.listdir(labels_folder):
    if label_file.endswith(".txt"):
        label_name = os.path.splitext(label_file)[0]
        if label_name in image_names:
            # Copy the label file to the output folder
            source_path = os.path.join(labels_folder, label_file)
            destination_path = os.path.join(output_folder, label_file)
            shutil.copy(source_path, destination_path)

print("Annotation files successfully copied to the output folder.")
