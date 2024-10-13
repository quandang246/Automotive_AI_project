import glob2
import numpy as np
import os

# Setting
path = "/home/quandang/project/Automotive_AI_project/darknet/data"  # Project's path
os.chdir(path)

#---------Data preprocess-----------

# Define the data folders
data_folders = ["label_cigarette", "label_phone(verified)", "seatbetl_v1"]

# Collect all image files from the specified folders
all_files = []
for ext in ["*.png", "*.jpeg", "*.jpg"]:
    for class_data in data_folders:
        images = glob2.glob(os.path.join(path, class_data, ext))  # Use 'path' for correct subfolder
        all_files.extend(images)

print("Number of frames: {} ".format(len(all_files)))

# Split validation data
valid_ratio = 30
rand_idx = np.random.choice(len(all_files), size=int(len(all_files) * valid_ratio / 100), replace=False)

# Create train.txt
with open(os.path.join(path, "train.txt"), "w") as f:
    for idx in range(len(all_files)):
        if idx not in rand_idx:  # Only write training data
            f.write(all_files[idx] + '\n')

# Create train.txt
with open("train.txt", "w") as f:
    for idx in range(len(all_files)):
        if idx not in rand_idx:  # Only write training data
            f.write(all_files[idx] + '\n')

# Create valid.txt
with open(os.path.join(path, "test.txt"), "w") as f:
    for idx in rand_idx:
        f.write(all_files[idx] + '\n')

with open("test.txt", "w") as f:
    for idx in rand_idx:
        f.write(all_files[idx] + '\n')

# Create obj.names config file
classes = ["cigarette", "phone", "seatbetl"]

with open(os.path.join(path, "obj3.names"), "w") as f:
    for cls in classes:
        f.write(cls + '\n')

with open("obj3.names", "w") as f:
    for cls in classes:
        f.write(cls + '\n')


# Config obj.data config file
cfg_data = [
    "classes={}".format(len(classes)),
    "train=train.txt",  # Adjusted to the correct path
    "valid=test.txt",   # Adjusted to the correct path
    "names=obj3.names", # Corrected filename
    "backup=backup/"
]

with open(os.path.join(path, "obj3.data"), "w") as f:
    for line in cfg_data:
        f.write(line + '\n')

with open("obj3.data", "w") as f:
    for line in cfg_data:
        f.write(line + '\n')
