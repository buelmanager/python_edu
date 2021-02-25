# if
#whether = "비"
# whether = input("오늘의 날씨는 어떤가요?")

# if whether == "비" or "눈" :
#     print("우산을 챙기세요.")
# elif whether == "미세먼지" : 
#     print("마스크를 챙기세요.")
# else :
#     print ("준비물이 없습니다.")
    
temp = int(input("기온이 어때요?"))
if 30 <= temp :
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else :
    print("너무추워요. 나가지 마세요.")