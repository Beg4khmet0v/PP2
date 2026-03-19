import shutil
from pathlib import Path

# create folders
Path("source").mkdir(exist_ok=True)
Path("destination").mkdir(exist_ok=True)

# create sample file
with open("source/example.txt", "w") as f:
    f.write("Hello Practice 6")

# copy file
shutil.copy("source/example.txt", "destination/example_copy.txt")

# move file
shutil.move("destination/example_copy.txt",
            "destination/moved_example.txt")

print("File copied and moved successfully")