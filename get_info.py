import requests
from bs4 import BeautifulSoup


urls = ['http://www.vipveg.com/price/2018/all/m{}d-1cta351by-1p{}.html'.format(str(m),str(p)) for m in range(1,2) for p in range(1,3)]

for url in urls:

    wb_data = requests.get(url)
