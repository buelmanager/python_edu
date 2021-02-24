# 사전
caibinet = { 
    1:"man1",
    100:"man2"           
}

print(caibinet)
print(caibinet[1])
print(caibinet.get(100))

#print(caibinet[5])                 # Error
print(caibinet.get(5))              # None
print(caibinet.get(5,"빈사물함"))     # 빈사물함

print ( 1 in caibinet)  # True
print ( 5 in caibinet)  # False

caibinet = { "a-1" : "man1" , "b-100" : "man2" , "c-1" : "man3"}
print(caibinet["a-1"])

# 새로운 사람
caibinet["a-1"] = "man4"
caibinet["a-2"] = "man5"

print(caibinet)

# 지우기
del caibinet["a-1"]
print(caibinet)

#key 만 출력
print (caibinet.keys())

# value 만 출력
print ( caibinet.values())

# key, value 쌍으로 출력
print ( caibinet.items())

# 삭제
caibinet.clear()
print(caibinet)