import difflib
import os


with open("myfile.txt", 'r') as file1:
  file1_contents = file1.readlines();
file1 = open('myfile.txt', 'r+')
file2 = open('compareTest.txt', 'r+')

text1 = file1.read(100)
text2 = file2.read(100)
print(text1)
print(text2)

def compare_files(file1, file2):
  compare = filecmp.cmp(file1, file2)

  if compare == True:
    print("The files are the same.")
  else:
    print("The files are different.")

compare_files(file1, file2)

