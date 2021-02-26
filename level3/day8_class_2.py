#class

#일반유닛
class Unit:
    #생성자 
    def __init__(self,name,hp,damage):
        self.name=name  # 멤버 변수
        self.hp=hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage))
        
        

marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)

#레이스 : 공중유닛, 클로킹
wraith1 = Unit("레이스", 80, 5)
print(" 유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

#레이스 : 공중유닛, 클로킹
wraith2 = Unit("클로킹 레이스", 80, 5)
print(" 유닛이름 : {0}, 공격력 : {1}".format(wraith2.name, wraith2.damage))
wraith2.clocking = True # 변수 추가 할당

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
    
    
# 공격유닛
class AttackUnit:
    #생성자 
    def __init__(self,name,hp,damage):
        self.name=name  # 멤버 변수
        self.hp=hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage))
        
    def attacked(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [ 공격력 {2} ]".format(self.name,location,self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if(self.hp <= 0):
            print("{0} 유닛이 파괴되었습니다.")
            
#파이어뱃 공격유닛 / 화염방사기
firebat1 = AttackUnit("파이어뱃",50,16)
firebat1.attacked("5시")

firebat1.damaged(25)
firebat1.damaged(25)