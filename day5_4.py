# continu 와 break
students = range(1,21)
absent = [2,5] # 결석 
nobook = [7]

for student in students :
    if student in absent :
        continue
    elif student in nobook :
        print( "{0} 번 교무실로와.".format(student))
        break
    print( "{0} 번 책읽어봐.".format(student))
    
# 한줄 for 
student = [1,2,3,4,5]
print(student)

students = [ i+100 for i in student]
print(students)