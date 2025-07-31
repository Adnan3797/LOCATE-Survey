import os

# Define the path to your labels folder
labels_folder = "./labels/"
output_file = "images.txt"  # Name of the output file

txt_files = [
    os.path.splitext(file)[0]
    for file in os.listdir(labels_folder)
    if file.endswith(".txt")
]


with open(output_file, "w") as f:
    for name in txt_files:
        f.write(name + "\n")
print(f"File names saved to {output_file}.")
