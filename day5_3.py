#while
# customer = "man"
# index = 5

# while index >= 1 :
#     print ( "{0}, 커피가 준비되었습니다. {1} 번남았어요.".format(customer,index))
#     index -= 1
    
#     if index == 0: print("커피가 폐기처분되었습니다.")


# 무한루프     컨트롤 + c로 빠져나옴 // 디버깅 정지 
# index = 5 
# while index >= 1 :
#     print ( "{0}, 커피가 준비되었습니다. {1} 회.".format(customer,index))
#     index += 1
 
#사용자 대답에 따른 
customer = "토르"
person = "Unknown"

while customer != person :
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")