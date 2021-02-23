# 문자열

sentence = '나는 소년입니다.'
print ( sentence)

sentence2 = "파이썬은 쉬워요."
print( sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요.
"""

print(sentence3)

# 슬라이싱

jumin = "820306-1155711"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])           # 0부터 2직전
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])        # 처음부터 6직전
print("뒤 7자리 : " + jumin[7:14])      
print("뒤 7자리 : " + jumin[7:])        # 7부터 끝까지 
print("뒤 7자리 (뒤에서부터): " + jumin[-7:])   # 맨뒤에서 7번째부터 문자열 끝까지 

# 문자열 처리함수 

python = "Python is Amazing"

print ( python.lower())
print ( python.upper())
print ( python[0].isupper())
print ( len(python))
print ( python.replace("Python", "Java"))

index = python.index("n")
print(index)

index = python.index("n",index + 1)
print (index)

print ( python.find("Java"))
#print (python.index("Java"))    # Error

print(python.count("n"))

## 문자열 포멧

print("a" + "b")

#방법 1
print ("나는 20살입니다.")

print ("나는 %d살입니다." % 20) #정수값만
print ("나는 %s을 좋아해요." % "파이썬") #문자열 

print ( "Apple 은 %c 로 시작해요." % "A") #한자리 문자

print ("나는 %s살입니다." % 20) #정수도 가능

print("나는 %s 색과 %s 색을 좋아해요." % ("파란" , "빨간"))

#방법 2

print ("나는 {}살 입니다." .format(20))
print ("나는 {} 색과 {} 색을 좋아해요." .format ("파란" , "빨간"))
print ("나는 {0} 색과 {1} 색을 좋아해요." .format ("파란" , "빨간"))
print ("나는 {1} 색과 {0} 색을 좋아해요." .format ("파란" , "빨간"))

#방법 3
print ("나는 {age}살이며 {color} 색을 좋아해요." .format (age = 20 , color = "빨강"))

#방법 4
age = 20
color = "빨강"
print (f"나는 {age}살이며 {color} 색을 좋아해요.")

# 탈출문자 

# \n :줄바꿈
print ("백문이 불여일견\n백문이 불여일타")

# \" \'
print (" \"백문이 불여일견\" \"백문이 불여일타\" ")

# \\ => \
print ("c:\\users\\")

# \r : 커서를 맨앞으로 이동
print ("Red Apple\rPine") # PineApple

# \b : 백스페이스 
print ("Redd\bApple") # RedApple

# \t : tab
print ("Red\tApple")

''' 
퀴즈 : 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
예)http://namver.com
규칙1 : http://     부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처름 세자리 + 글자 갯수 + 글자내 'e' 갯수 + '!'로 구성
            nav                 5          1          ! 
생성 예)nav51!
'''

sitename = "http://google.com"

#split
myStr = sitename.split("://")[1]
print("step #1 : " + myStr)

myStr = myStr.split(".")[0]
print("step #2 : " + myStr)

myStr = myStr[0:3] + str(len(myStr)) + str(myStr.count('e')) + "!"
print("step #3 :" + myStr)

# index and replace
myStr = sitename.replace( "http://", "")
print (myStr)

myStr = myStr[:myStr.index(".")]
print (myStr)

myStr = myStr[0:3] + str(len(myStr)) + str(myStr.count('e')) + "!"
print("step #3 :" + myStr)