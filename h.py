#환경설정 
#install python 
#install visual code
#install python plugin in visual code

# from level6.travel.thailand import ThailandPackage
from level6.travel import *

tl = vietnam.VietnamPackage()
tl.detail()

import inspect

#파일 위치확인
print(inspect.getfile(thailand))

#import Beautifulsoup4