# 표준입출력 
print("java","kotlin","javascript" , sep=(" vs ") , end=("? "))
print("무엇이 더 재미있을까요?")

# sys
import sys
print ("Android",file=sys.stdout)   #표준출력
print ("Android",file=sys.stderr)   #표준에러

# print format 
scores = { "수학":1, "영어":90, "체육":100}
for subject, score in scores.items():
    #print (subject,score)
    #print ()
    print ( subject.ljust(8), str(score).rjust(4),sep=(":"))
    
# add zero
for num in range(1,21):
    print ( "대기번호 : " + str(num).zfill(3))