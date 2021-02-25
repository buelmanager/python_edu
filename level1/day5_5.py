#퀴즈
'''
당신은 cocoa 서비스를 이용하는 택시 기사입니다.
50명의 승객과 매칭 기회가 있을때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

조건1 : 승객별 운행 소요시간은 5~50분 사이 난수
조건2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 55분)
[O] 3번째 손님 (소요시간 : 15분)
[ ] 4번째 손님 (소요시간 : 25분)

'''

from random import *
customers = []

for i in range(51):
    user = {
        "name" : i,
        "delay" : randint(5,51)
    }
    
    customers.append(user)
    
print ( "cuscomers : " + str (customers))

user_cnt = 0
for cuscomer in customers :
    if 5<= cuscomer["delay"] <= 15 :
        print ("[O] {0} 손님 승차할수 있습니다. 소요시간은 {1}".format(cuscomer["name"] ,cuscomer["delay"]))
        user_cnt += 1
    else :
        print ("[ ] {0} 손님 승차할수 없습니다! 소요시간은 {1}".format(cuscomer["name"] ,cuscomer["delay"]))
        
print("총 탑승인원은 " + str(user_cnt))