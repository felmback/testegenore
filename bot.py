

import requests
from bs4 import BeautifulSoup as bs


url ="https://www.casasbahia.com.br/c/eletrodomesticos/refrigeradores?filtro=c13_c14_l10037&nid=201602&utm_source=gp_pla&utm_medium=cpc&gclsrc=aw.ds&&utm_campaign=gg_pmax_core_eldo&gad_source=1&gclid=Cj0KCQjwjLGyBhCYARIsAPqTz1-81ObiuMBIfxIbFfF1nNwszsL0fgKu4NFJGIZxiVn9l5LUv3dsAscaAguCEALw_wcB"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
            
r = requests.get(url,headers=headers)

soup = bs(r.content,"html.parser")

print(soup.prettify())

produto = soup.find_all("div",class_="css-1enexmx")
preco = soup.find_all("div",class_="product-card__details-wrapper")
for p in produto:
    print(p.text)
    p.split()