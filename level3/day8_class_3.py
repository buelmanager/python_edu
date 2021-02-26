#상속

#일반유닛
class Unit:
    #생성자 
    def __init__(self,name,hp):
        self.name=name  # 멤버 변수
        self.hp=hp  
        
# 공격유닛
class AttackUnit(Unit):
    #생성자 
    def __init__(self,name,hp,damage):
        Unit.__init__(self,name,hp)
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