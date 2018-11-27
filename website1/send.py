import requests

headers={}
headers['Authoraization']= 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMSIsImV4cCI6MTU0MzQyOTg1MiwicmVmcmVzaF9leHAiOjE1NDM5NDgyNTJ9.c0P5SNM5vGvCrOQA778fVq2HQXYoRwhayaHAONqc5ms'
r = requests.get('http://127.0.0.1:8000/api/token/refresh', headers=headers)
print(r.text)