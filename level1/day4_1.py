# 튜플 
color = ( "red" , "blue")

print ( color[0])

# name = "man"
# old = 20
# hobby = "read"

# print(name,old,hobby)

(name, old , hobby) =  ("man" , 20 , "read")
print(name,old,hobby)

# set (집합)
my_set = {1,2,3,3,3,3}
print (my_set)

my_set2 = set([1,5,6,7,7,7,7])
print (my_set2)

# 교집합
print( my_set & my_set2)
print ( my_set.intersection(my_set2))

# 합집합 
print ( my_set or my_set2)
print ( my_set.union(my_set2))

# 차집합 
print ( my_set - my_set2)
print ( my_set.difference(my_set2))

# 추가
my_set2.add( 8)
print(my_set2)

# 삭제
my_set2.remove(7)
print(my_set2)