#day 1

#숫자 자료형 
print(5)

#문자 자료형
print("문자")
print("문자"*9)

# 참 / 거짓 
print ( True )
print ( 5 > 10 )
print ( not True)
print ( not ( 5 > 10))

# 변수 

print ("----- 변수 사용이전 ------")
print ("나의 이름은 사과입니다.")
print ("사과 은/는 빨강색입니다.")
print ("사과 이/가 이곳에 온지 10일 되었습니다.")
print ("사과 을/를 산지 오래되었나요? True")

print ("----- 변수 사용이후 ------")

color = "red"
name = "apple"
date = 10
is_old = date >= 10

print ("나의 이름은 "+name+"입니다.")
print (name + " 은/는 색상은 "+ color+ "입니다.")
print (name+ " 이/가 이곳에 온지 "+ str(date)+"일 되었습니다.")
print (name+ " 을/를 산지 오래되었나요? " + str(is_old))

# 주석 
# 실행이 안되는 부분 / 설명을 위한 부분 

''' 
여러문장 주석처리
'''

'''
문제 : 변수를 이용하여서 다음 문장을 출력하시오

변수명 : station

변수값 : "사당", "신도림", "인천공항" 순서대로 입력

출력문장 : 
  OOO 행 열차가 들어오고 있습니다.
'''

