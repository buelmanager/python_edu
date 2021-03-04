class ThailandPackage:
    def detail(self):
        print ("[태국 패키지 3박5일 50만원]")
        
        
# 패키지
## __name__ , __main__

if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    
    trip_to = ThailandPackage()
    trip_to.detail()
else :
    print("Thailand 외부에서 호출되는 경우")