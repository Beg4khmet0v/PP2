f = open("demofile.txt")
print(f.read()) #1st example
f.close() #4th example, closing

#f = open("Practice 6/file_handing/demofile.txt")
#print(f.read()) #2nd example, doesn't work

with open("demofile.txt") as f:
  print(f.read()) #3rd example

with open("demofile.txt") as f:
  print(f.read(5)) #5th example

with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline()) #6-7th examples

with open("demofile.txt") as f:
  for x in f:
    print(x) #final one