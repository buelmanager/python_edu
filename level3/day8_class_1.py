# 마린 : 공격 유닛, 군인, 총을 쏠수 있음

name = "마린" # 유닛이름
hp = 40 # 유닛체력
damage = 5 # 유닛의 공격력

print("{0}유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# 탱크 : 공격 유닛, 포를 쏠수있음, 일반/시즈 모드

tank_name = "탱크" # 유닛이름
tank_hp = 150 # 유닛체력
tank_damage = 35 # 유닛의 공격력

print("{0}유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

tank2_name = "탱크2" # 유닛이름
tank2_hp = 150 # 유닛체력
tank2_damage = 35 # 유닛의 공격력

print("{0}유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp,tank2_damage))


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name,location,damage))
    
attack( name,"1시",damage)
attack( tank_name,"1시",tank_damage)
attack( tank2_name,"1시",tank2_damage)