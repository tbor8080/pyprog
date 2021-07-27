import os, sys, requests
from modules import *

url='http://localhost:50000/insert'

res=requests.post(url, data={'aaa':123})
print(res.text)
