import os
import shutil
from pathlib import Path

Path("hz.dir").mkdir(exist_ok=True)

with open("hz.dir/hello.txt", "w") as f:
    f.write("Hello my name is Suzie")

with open("hz.dir/hello.txt", "r") as f:
    print(f.read())

shutil.copy("hz.dir/hello.txt", "hz.dir/bye.txt")

with open("hz.dir/bye.txt")