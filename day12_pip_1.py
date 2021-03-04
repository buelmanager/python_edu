# pip 
## pypi

## https://pypi.org/ 
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>Bad<i>HTML")
print(soup.prettify())