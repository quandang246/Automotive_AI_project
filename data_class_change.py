import os

# Define the folder containing the image and text files
folder_path = '/home/quandang/project/Automotive_AI_project/darknet/data/seatbetl_v1'
class_id = 2

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image (you can add more extensions if needed)
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Create the corresponding text file name
        text_file = os.path.splitext(filename)[0] + '.txt'
        text_file_path = os.path.join(folder_path, text_file)

        # Check if the corresponding text file exists
        if os.path.exists(text_file_path):
            with open(text_file_path, 'r') as file:
                # Read the lines of the text file
                lines = file.readlines()

            # Modify the first element of each line from '0' to '1'
            new_lines = []
            for line in lines:
                # Split the line into elements
                elements = line.split()
                if elements:
                    # Change the first element from '0' to '1'
                    elements[0] = str(class_id)  # Change to '1'
                # Join the elements back into a single line
                new_lines.append(' '.join(elements) + '\n')

            # Write the modified content back to the file
            with open(text_file_path, 'w') as file:
                file.writelines(new_lines)
        else:
            # If the text file does not exist, delete the image file
            image_file_path = os.path.join(folder_path, filename)
            os.remove(image_file_path)
            print(f"Deleted image file {filename} because corresponding text file does not exist.")
