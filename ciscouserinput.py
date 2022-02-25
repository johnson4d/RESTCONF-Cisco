#!/usr/bin/python3.9

import requests
import json
import urllib3
import base64
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time
username = input("Username?")
password = input("Password?")
ip_address = input("IP Address?")

# This takes the username and password, base64 encodes it for authorisation...
username_password_string = username+":"+password
username_password_bytes = username_password_string.encode("ascii")
username_password_base64_bytes = base64.b64encode(username_password_bytes)
username_password_base64_string = username_password_base64_bytes.decode("ascii")

while True:

  url_1 = "https://"+ip_address+"/restconf/data/Cisco-IOS-XE-device-hardware-oper:device-hardware-data/device-hardware/device-system-data/current-time"
  url_2 = "https://"+ip_address+"/restconf/data/Cisco-IOS-XE-arp-oper:arp-data"

  payload={}
  headers = {
     'Content-Type': 'application/yang-data+json',
     'Accept': 'application/yang-data+json',
     'Authorization': "Basic "+username_password_base64_string+""
   }
  response_1 = requests.request("GET", url_1, headers=headers, data=payload,verify=False)
  print(response_1.text)
  response_2 = requests.request("GET", url_2, headers=headers, data=payload,verify=False)
  print(response_2.text)
  time.sleep(10) # Sleep for 10 seconds
