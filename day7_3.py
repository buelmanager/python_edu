# 파일출력 

## 쓰기
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 10", file=score_file)
# score_file.close()

## 추가
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 10")
# score_file.close()

## 읽기 모두
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close();

## 읽기 한줄
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())

score_file.close();

## 읽기 반복문으로 읽기
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line) 
score_file.close();

## 읽기 리스트로 담기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 리스트 형태
for line in lines:
    print(line)

score_file.close();