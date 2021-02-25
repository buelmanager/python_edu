# 퀴즈

'''
    당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
    보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
    
    - X 주차 주간보고 - 
    
    부서 :
    이름 :
    업무 요약 :
    
    1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오
    조건 : 파일명은 1주차.txt 와 같이 만듭니다.
    
'''
import os
import errno

week_num = 0

while True:
    week_num += 1
    if week_num > 50:
        break
    
    #파일이 많아 폴더에 넣는것을 추가하였고,
    #폴더가 없는경우 에러가 발생하여서 예외처리를 하였다.
    ##################################################################
    completeName = os.path.join("work", "{0}주차.txt".format(week_num))
    if not os.path.exists(os.path.dirname(completeName)):
        try:
            os.makedirs(os.path.dirname(completeName))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    ##################################################################       
    with open(completeName,"w",encoding="utf8") as work_file:
        work_file.write( '''
    - {0} 주차 주간보고 - 

    부서 :
    이름 :
    업무 요약 :
        '''.format(week_num))