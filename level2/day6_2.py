# 퀴즈

'''
    표준 체중  각 개인의 키에 적당한 체중
    
    (성별에 따른 공식)
    남자 : 키 x 키 x 22
    여자 : 키 x 키 x 21
    
    조건1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
    조건2 : 표준 체중은 소수점 둘째자리까지 표시
    
    (출력 예제)
    키 175cm 인 남자의 표준 체중은 67.38kg 입니다.
    
'''

def std_weight (height,gender):
    if gender == "남자" : 
        return pow(height,2)*22
    else :
        return pow(height,2)*21

gender = input("당신의 성별은 무엇입니까? (남자/여자) : ")
height = int(input("키는 몇 cm입니까? (cm) : "))

weight = round(std_weight( height/100,gender),2)
print("키 {0}cm 인 {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,weight))
