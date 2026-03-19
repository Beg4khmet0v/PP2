with open("Practice 6/file_handing/demofile.txt", "a") as f:
   f.write("Now the file has more content!")

#open and read the file after the appending:
with open("Practice 6/file_handing/demofile.txt") as f:
  print(f.read()) #1st example



with open("Practice 6/file_handing/demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("Practice 6/file_handing/demofile.txt") as f:
  print(f.read()) #2nd example

f = open("myfile.txt", "w")
f.write("Now the file has more content!")
f.close() #3rd example (changed)

f = open("myfile.txt", "r")
print(f.read())
f.close() #my own example