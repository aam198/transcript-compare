import difflib

with open("myfile.txt", 'r') as file1:
  file1_contents = file1.readlines()
with open("compareTest.txt", 'r') as file2:
  file2_contents = file2.readlines()

diff = difflib.unified_diff(
  file1_contents, file2_contents, fromfile = "file1.txt",
  tofile = "file2.txt", lineterm=''
)

for line in diff:
  print(line)

with open("student_gpa_2019.txt", 'r') as file3:
  file3_contents = file3.readlines()
with open("student_gpa_2020.txt", 'r') as file4:
  file4_contents = file4.readlines()

difference = difflib.unified_diff(
  file3_contents, file4_contents, fromfile = "file3.txt",
  tofile="file4.txt", lineterm= ''
)

for line in difference:
  print(line)

# file1 = open('myfile.txt', 'r+')
# file2 = open('compareTest.txt', 'r+')

# text1 = file1.read(100)
# text2 = file2.read(100)
# print(text1)
# print(text2)



