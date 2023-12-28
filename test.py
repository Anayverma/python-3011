l=[]
print("enter name seperated by whitespace")
p=input().split()
marks=[]
sum=0
for i in range(5):
    print("Enter {}'s marks".format(p[i]))
    row=[]
    for j in range(5):
        a,m,l=list(map(int ,input("enter marks of assignments, Midterm test, and lab work of subject {} seperated by whitespace".format(j+1)).split()))
        avg=.1*a+.7*m+.2*l
        if avg >=90:
            row.append("O")
        elif avg>=80:
            row.append("A")
        elif avg>=70:
            row.append("B")
        else:
            row.append("C")
        sum+=avg
    marks.append(row)
avg=sum/25
if avg >=90:
        class_grade="O"
elif avg>=80:
        class_grade="A"
elif avg>=70:
        class_grade="B"
else:
        class_grade="C"
for i in range (5):
    print("Enter {}'s Grade are --".format(p[i]))
    for j in range(5):
           print("Subject {}'s Grade -- ".format(marks[i][j]))
    print()
print("class average is {} and its grade is {}".format(avg,class_grade))
           
       
