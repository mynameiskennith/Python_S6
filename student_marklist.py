n = int(input('Enter the number of students : '))
marklist={}
for i in range(n):
    name = input('Enter the student name :')
    marklist[name]=int(input('Enter the mark of {name} :'))
print('Mark List of Stdudents :')
for i in marklist:
    print(i,' : ',marklist[i])
