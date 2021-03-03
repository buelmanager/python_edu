# super 

#일반유닛
class Unit:
    #생성자 
    def __init__(self,name,hp,speed):
        self.name=name  # 멤버 변수
        self.hp=hp  
        self.speed = speed
        
    def move(self, location):
        print("[ 지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [ 속도 {2}]".format(self.name,location,self.speed))
        
        
# 공격유닛
class AttackUnit(Unit):
    #생성자 
    def __init__(self,name,hp,speed, damage):
        Unit.__init__(self,name,hp, speed)
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

#날수있는 기능을 가진 클래스    
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("[0} : {1} 방향으로 날아갑니다. [ 속도 {2} ]".format(self.name, location, self.flying_speed))
         
#날수있는 기능을 가진 클래스    
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [ 속도 {2} ]".format(name, location, self.flying_speed))
                
# 공중 공격유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name,hp, 0,damage)
        Flyable.__init__(self,flying_speed)
        
    def move(self, location):
        print("[ 공중 유닛 이동]")
        Flyable.fly(self, self.name,location)
        
        
# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        
        #다중 상속일 경우는 1의 경우처럼 명시적으로 사용을 하고
        #한개만 있을때는 1또는 2의 방법을 택한다.
        
        #1. 
        # Unit.__init__(self,name,hp,0)
        
        #2.
        super().__init__(name,hp,0)
        self.location = location