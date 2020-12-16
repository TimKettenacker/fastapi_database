#!/usr/bin/env python3
# test the FastAPi by creating some POST and GET requests

import requests
import json

payload = {"email": "latinlover99@hotmail.com", "password": "root"}
r = requests.post("http://127.0.0.1:8000/users/", data=json.dumps(payload))
if r.status_code == '200':
    print("User created successfully!")

r = requests.get("http://127.0.0.1:8000/users/")
print(r.json())