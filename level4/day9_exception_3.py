# 사용자 정의 예외처리

# class BigNumberError(Exception):
#     pass

# try:
#     num1 = int ( input("첫 번째 숫자를 입력하세요."))
#     num2 = int ( input("두 번째 숫자를 입력하세요."))
    
#     if(num1 >= 10 or num2 >= 10):
#         raise BigNumberError
    
#     print ( "{0} / {1} = {2}".format(num1 , num2 , num1/num2))
# except BigNumberError:
#     print ("잘못된 값을 입력하셨습니다. 한자리 숫자만 입력하세요.")


class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
        
try:
    num1 = int ( input("첫 번째 숫자를 입력하세요."))
    num2 = int ( input("두 번째 숫자를 입력하세요."))
    
    if(num1 >= 10 or num2 >= 10):
        raise BigNumberError("입력값 : {0}, {1}".format(num1,num2) )
    
    print ( "{0} / {1} = {2}".format(num1 , num2 , num1/num2))
except BigNumberError as err:
    print ("잘못된 값을 입력하셨습니다. 한자리 숫자만 입력하세요.")
    print (err)

finally:
    print("계산기를 이용해 주셔서 감사합니다.")