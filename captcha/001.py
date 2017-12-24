# -*- coding:utf-8 -*-
import sys

__author__ = 'IanChen'

# import pytesseract
# from PIL import Image
#
# im = Image.open("code.jpg")
# im = im.convert("L")
#
#
# def initTable(threshold=140):
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#
#     return table
#
#
# # binaryImage = im.point(initTable(), '1')
# # binaryImage.show()
# tmp=pytesseract.image_to_string(im)
# print(tmp)
import requests
from multiprocessing.pool import ThreadPool

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
postdata = {"BatchID": 45,
            "BatchYear": 2017,
            "BatchMonth": 7,
            "CompanyID": 18282900,
            "CustomerID": 9,
            # "TaxId":440300754285743,
            "TaxId": 440300771615767,
            "TaxPwd": 83093013,

            # "TaxPwd":77766683,
            'jobname': '工程1',
            'jobparams': "工作中"
            }
pool = ThreadPool(processes=20)



# def sb():
#     print('开始任务')
re = requests.post(url="http://120.79.65.131:8000/search-post", data=postdata, timeout=200)
print(re.text)
#     sys.exit()


# re = requests.post(url="http://127.0.0.1:8000/search-post", data=postdata)
# a = 0
# while a < 100:
#     a += 1
#     pool.apply_async(sb)
# print('over')
# pool.close()
# pool.join()
