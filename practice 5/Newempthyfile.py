import re

text = "Some kind of word"
pattern1 = "\.*\d"
result=re.findall(pattern1, text)
print(result)