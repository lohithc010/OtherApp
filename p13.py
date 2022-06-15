student = {}
c=0
for i in range(5):
    k = input("Enter the student field:\n")
    v = input("enter {} value name:\n".format(k))
    student[k] = v
    # student.setdefault(k,v)
    c=c+1 

print(student)