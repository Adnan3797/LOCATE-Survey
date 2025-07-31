import os

# Define the path to your folder containing the .txt files
folder_path = "./labels/"

# Output file where all contents will be merged
output_file = "merged_output.txt"

# Open the output file in write mode
with open(output_file, "w", encoding="utf-8") as outfile:
    # Iterate over each file in the folder
    for filename in sorted(os.listdir(folder_path)):
        # Check if the file is a .txt file
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            # Open and read the content of the .txt file
            with open(file_path, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                outfile.write("\n")  # Add a newline character to separate contents

print(f"All .txt files have been merged into {output_file}.")
