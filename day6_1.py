# 함수

def open_account():
    print("새로운 계좌가 생성됩니다.")
    
## 전달값과 반환값 
def deposit(balance , money):
    print ("입금이 완료. 잔액은 {0}원".format(balance + money))
    return balance + money

def withdraw(balance , money):
    if balance >= money:
        print ("출금이 완료되었습니다. 잔액은 {0}원".format(balance-money))
        return balance - money
    else :
        print ("출금이 완료되지 않습니다. 잔액은 {0}원".format(balance))
        return balance

def withdraw_night(balance, money):
    commision = 100
    if balance >= money+commision:
        print ("night 출금이 완료되었습니다. 잔액은 {0}원".format(balance-money-commision))
        return commision , balance - money - commision
    else :
        print ("night 출금이 완료되지 않습니다. 잔액은 {0}원".format(balance))
        return 0 , balance
    
balance = 0
balance = deposit(balance, 1000)
print(balance)

balance = withdraw(balance, 2000)
print(balance)

balance = withdraw_night(balance, 900)
print("수수료는 {0}이고, 잔액은 {1}입니다.".format(balance[0],balance[1]))

## 기본값 
def profile(name, age, main_lang):
    print ("이름 : {0}\t 나이 : {1}\t 주언어 : {2}"\
        .format(name, age, main_lang))
    
    
profile("man1",20, "java")
profile("man2",30, "python")


## 기본값 적용 
def profile(name, age=20, main_lang="python"):
    print ("이름 : {0}\t 나이 : {1}\t 주언어 : {2}"\
        .format(name, age, main_lang))
    
profile("man1")
profile("man2")

## 키워드 
profile(name="man3",main_lang="kotlin",age=30)

## 가변인자 
def profile(name, age, lang1, lang2, lang3):
    print ("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
    print ( lang1, lang2, lang3)
    

profile("man1",20, "java" , "C", "C#")
profile("man2",30, "python" ,"", "")

## 가변인자 사용
def profile(name, age, *langs):
    print ("이름 : {0}\t 나이 : {1}\t".format(name, age), end=" ")
    for lang in langs:
        print (lang , end=" ")
    print ()

profile("man1",20, "java" , "C", "C#", "kotlin" , "javascript")
profile("man2",30, "python" )

## 지역변수 / 전역 변수

gun = 10

def checkpoint (soldiers): # 경계근무
    #gun = 20
    global gun 
    gun = gun - soldiers                        #Exception has occurred: UnboundLocalError
                                                #local variable 'gun' referenced before assignment
    print("[함수 내] 남은총 : {0}".format(gun))
    
    
def checkpoint_ret (gun , soldiers): # 경계근무
    gun = gun - soldiers                                                
    print("[함수 내] 남은총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun , 2)
print("전체 총 : {0}".format(gun))