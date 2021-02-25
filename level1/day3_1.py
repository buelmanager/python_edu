# list

# 지하철 칸별로 10, 20, 30 명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["man1" , "man2" ,"man3"]
print(subway)

# man2가 타고있는 칸은?
print(subway.index("man2"))

# man4 추가로 다음칸에 탑승
subway.append("man4")
print (subway)

# 1번칸에 man5를 탑승
subway.insert(1,"man5")
print (subway)

# 맨뒤의 사람을 한명 꺼냄
print(subway.pop())
print(subway)

# 같은 사람이 몇명 있는지 확인
subway.append("man1")
print(subway)
print(subway.count("man1"))

# 정렬
num_list = [5,3,2,1,4]
num_list.sort()
print(num_list)

# 뒤집기
num_list.reverse()
print(num_list)

# 지우기 
#num_list.clear()
#print(num_list)

# 혼합가능
mix_list = ["man" , 1 ,True]

mix_list.extend(num_list)
print(mix_list)


