import os
from pathlib import Path

# current directory
print("Current directory:", os.getcwd())

# create directory
os.mkdir("test_dir")

# create nested directories
os.makedirs("test_dir/subdir1/subdir2", exist_ok=True)

# list files and folders
print("Contents:")
for item in os.listdir():
    print(item)

# change directory
os.chdir("test_dir")
print("Changed directory:", os.getcwd())