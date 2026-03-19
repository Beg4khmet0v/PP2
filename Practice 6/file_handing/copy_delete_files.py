import os
os.remove("Practice 6/file_handing/demofile.txt")

import os
if os.path.exists("Practice 6/file_handing/demofile.txt"):
   os.remove("Practice 6/file_handing/demofile.txt")
else:
  print("The file does not exist")

import os
os.rmdir("myfolder")