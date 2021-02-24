# 자료구조의 변경 

numbers = { 1,2,3,4}
print (numbers , type(numbers))

numbers = list(numbers)
print (numbers , type(numbers))

numbers = tuple(numbers)
print (numbers , type(numbers))

numbers = set(numbers)
print (numbers , type(numbers))

'''
퀴즈 : 당신의 학교헤서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글작성자들 중 추첨을 통해 1명은 치킨, 3명은 쿠폰을 받게 됩니다.
추천 프로그램을 작성하시오

조건1 : 편의상 댓글은 20명이 작성하고 아이디는 1~20 이라고 가정
조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복불가
조건3 : random ahebfdml shuffle 과 sample 을 활용

( 출력 예제 )
-- 당첨자 발표 --
치킨 : 1
커피 : [2,3,4]
-- 축하합니다. -- 


'''

from random import *
lst = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

lst = set(lst) 
lst = list(lst)
print(lst)
shuffle(lst)

chikin = lst.pop()
print("chikin : " + str(chikin))
print(lst)

coffe = sample ( lst , 3)
print ("coffe : " + str(coffe))

print (
'''
-- 당첨자 발표 --
치킨 : {chi}
커피 : {cof}
-- 축하합니다. -- 
'''.format( chi=chikin , cof = coffe)
)

###########################################

users = range ( 1, 21) # 1 ~ 20
print(users)

users = list(users)
print (users)

shuffle(users)
print (users)

winners = sample(users , 4)

print (
'''
-- 당첨자 발표 --
치킨 : {chi}
커피 : {cof}
-- 축하합니다. -- 
'''.format( chi=winners[0] , cof = winners[1:])
)
