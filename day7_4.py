# pickle

import pickle

## pickle write
# profile_file = open("profile.pickle" , "wb")
# profile = {"이름":"man1" , "나이":30, "취미":["축구", "농구", "야구"]}
# pickle.dump(profile,profile_file)
# profile_file.close()

## pickle read
profile_file = open("profile.pickle" , "rb")
profile = pickle.load(profile_file) # file 에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

## with
with  open("profile.pickle" , "rb") as profile_file:
    print (pickle.load(profile_file))
    
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("스터디를 열심히...")
    
with open("study.txt","r",encoding="utf8") as study_file:
   print(study_file.read())