from tkinter.filedialog import askopenfilename
import random

filename = askopenfilename()
lines = open(filename).readlines()
selectedStudents = []
emailsOfSelectedStudents = []
allStudents = []
for line in lines:
    student = line.split(",")
    allStudents.append(student)

while(len(selectedStudents)<=50):
    number = random.randint(1,189)
    selectedStudent = allStudents[number]
    if(selectedStudent in selectedStudents):
        pass
    else:
        selectedStudents.append(selectedStudent)

#write csv as the result
string = ""
f=open("SelectedRandomlyStudents.csv", "a+")
for student in selectedStudents:
    string = string + student[2] + "\n"
f.write(string)
