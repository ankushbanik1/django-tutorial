import json
import os
import requests

AUTH_ENDPOINT ='http://127.0.0.1:8000/api/auth/jwt/'
ENDPOINT ='http://127.0.0.1:8000/api/status/'
# image_path =os.path.join(os.getcwd(),'f.jpg')


data= {
    'username':'ankush',
    'password':'dashing2580'
}
r=requests.post(AUTH_ENDPOINT,data=data)

token=r.json()['token']
headers={

     "Content-Type": "application/json" ,
     'Authorization' : 'JWT'+ token
}

post_data=json.dumps({'content':'some random content'})
posted_response= requests.post(ENDPOINT,data=post_data,headers=headers)
print(posted_response.text)

# get_endpoint=ENDPOINT+str(12)
