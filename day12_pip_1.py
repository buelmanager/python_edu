# pip 
## pypi

## https://pypi.org/ 
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>Bad<i>HTML")
print(soup.prettify())

## 내장함수 

## input

## dir : 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
import random
print(dir())
print(dir(random))

lst = [1,2,3]
print(dir(lst))

name = "jim"
print(dir(name))

## 외장함수 

## glob : 경로 내의 폴더 / 파일 목록 조회 ( 윈도우 dir )
import glob
print (glob.glob("*.py"))

## os : 운영체제에서 제공하는 기본 기능
import os
print (os.getcwd())  # guswo elfprxhfl 

folder = "sample"
if os.path.exists(folder):
    print("존재")
else :
    os.makedirs(folder) # 폴더 생성 

print (os.listdir())


## time : 
import time 
print (time.localtime())
print (time.strftime("%Y-%m-%d %H:%M:%S"))

## datetime
import datetime
print("오늘의 날짜는", datetime.date.today())

## timedelta : 두날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100) # 100일 저장
print ( "우리가 만난지 100일은" , today + td) ## 오늘부터 100일 
