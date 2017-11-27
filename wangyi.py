# -*- coding:utf-8 -*-
__author__ = 'IanChen'

import requests
import re
from bs4 import BeautifulSoup
from lxml import etree

url = 'http://www.163.com/'
resp = requests.get(url)
# soup= BeautifulSoup(resp.content,'html.parser')
# print(soup)
# data=soup.findAll('div',{'class':'bd'})
# match=re.findall(r'<a .*?>(.*?)</a>',str(data[0]))
# print(match)

# data=soup.findAll('div',{'class':"tab_panel current"})
# match=re.findall(r'<a href=(.*?)>(.*?)</a>',str(data[1]))
# print(match)

resp.encoding= 'utf-8'
root = etree.HTML(resp.content)#将request.content 转化为 Element
select= root.xpath('//div[@class="cm_area ns_area_top"]//div[@class="bd"]//li/a')
for i in select:

    title=i.xpath('./text()')[0]
    url=i.xpath('./@href')[0].replace('1','a')
    #当有多个属性时，用/./span[contains(@class,'vote')],意为span的class属性包含有值为vote
# selec=selec.xpath('./@href')[0]

    print(title)
    print(url)

pass
