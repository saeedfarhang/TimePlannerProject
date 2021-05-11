import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api/accounts'
headers = {
    'Content-Type':'application/json'
}

# CREATE USER
data = {
    'email':"s2@s.com",
    'name':'ss',
    'password':"password",
    'password2': 'password'
}

# r = requests.post(f"{BASE_URL}/register/",data=json.dumps(data), headers=headers)
# print(r.text)


# RETREVE ACCESS TOKEN

data2 = {
    'email':'s2@s.com',
    'password':'password'
}

r2 = requests.post(f"{BASE_URL}/token/",data=json.dumps(data2), headers = headers)
print(json.loads(r2.text)['access'])