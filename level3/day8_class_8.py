import random

#일반유닛
class Unit:
    #생성자 
    def __init__(self,name,hp,speed):
        self.name=name  # 멤버 변수
        self.hp=hp  
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
        
    def move(self, location):
        print("[ 지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [ 속도 {2}]".format(self.name,location,self.speed))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        if(self.hp <= 0):
            print("{0} 유닛이 파괴되었습니다.")    
        
# 공격유닛
class AttackUnit(Unit):
    #생성자 
    def __init__(self,name,hp,speed, damage):
        Unit.__init__(self,name,hp, speed)
        self.damage = damage
        print("체력 {0}, 공격력 {1}\n".format(self.hp,self.damage))
        
    def attacked(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [ 공격력 {2} ]".format(self.name,location,self.damage))
    
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    #스팀팩 : 체력을 10감소하고, 일정시간동안 이동/공격속도 증가
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print ("{0} : 스팀팩을 사용합니다. (체력 10감소)".format(self.name))
        else :
            print ("{0} : 체력이 부족하여 스팀팩을 사용할수 없습니다.".format(self.name))

class Tank(AttackUnit):
    
    seize_develop = False #시즈모드 개발여부
    
    def __init__(self):
        super().__init__("탱크", 150, 3 , 35)
        self.seize_mode = False
        
    #시즈모드 : 고정시켜 공격력 오름
    def set_seize_mode(self):
        
        if self.seize_develop == False:
            return 
        
        if self.seize_mode == False:
            self.damage *= 2
            self.seize_mode = True
            print ("{0} : 시즈모드로 전환합니다.".format(self.name))
        else :
            self.damage /= 2
            self.seize_mode = False
            print ("{0} : 시즈모드를 해제합니다.".format(self.name))
            
    
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
        
        
#레이스 
class Wraith(FlyableAttackUnit):
    
    # 클로킹 : 안보임
    clocking_develop = False
    
    def __init__(self):
        super().__init__("레이쓰", 80, 20 , 5)
        self.clocking = False
        
    def set_clocking_mode(self):
        
        if self.clocking_develop == False:
            return
        
        if self.clocking == False:
            self.clocking = True
            print ("{0} : 클로킹 설정 되었습니다.".format(self.name))
            
        else :
            self.clocking = False
            print ("{0} : 클로킹 해제 되었습니다.".format(self.name))
            
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
    
def game_over():
    print("Player : gg") # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")
    

# 게임진행
game_start()

# 마린
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 
t1 = Tank()
t2 = Tank()
 
# Tank seize mode develop
Tank.seize_develop = True
print ("Tank 시즈모드개발이 완료되었습니다. ")
# Wraith clocking mode develop
Wraith.clocking_develop = True 
print ("Wraith 클로킹 개발이 완료되었습니다. ")

# 레이스 
w1 = Wraith()

# 유닛 일괄 관리 ( 생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전체 유닛이동 
for unit in attack_units:
    unit.move("1시")

# 전체 유닛 공격 준비
for unit in attack_units:
    if isinstance(unit , Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.set_clocking_mode()
    
# 전체 유닛 공격
for unit in attack_units:
    unit.attacked("1시")
    
# 전체 피해
for unit in attack_units:
    unit.damaged(random.randint(5, 21)) # 공격은 랜덤으로 5 ~ 20

# 게임종료 
game_over()