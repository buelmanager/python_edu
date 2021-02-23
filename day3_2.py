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
