# 예외처리 
# print ("나누기 전용 프로그램")
# try:
#     num1 = int ( input("첫 번째 숫자를 입력하세요."))
#     num2 = int ( input("두 번째 숫자를 입력하세요."))
#     print ( "{0} / {1} = {2}".format(num1 , num2 , num1/num2))
# except ValueError:
#     print (" 에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print (err)

## 예외처리 2

print ("나누기 전용 프로그램")
try:
    nums = []
    nums.append(int ( input("첫 번째 숫자를 입력하세요.")))
    nums.append(int ( input("두 번째 숫자를 입력하세요.")))
    #nums.append(nums[0]/nums[1]) # 에러발생
    print ( "{0} / {1} = {2}".format(nums[0] , nums[1] , nums[2]))
except ValueError:
    print (" 에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print (err)
    
except Exception as err:
    print("알수없는 에러 발생 ! ")
    print(err)