# Script creates a VPN for a customer called Telstra. Data is taken from a seperate JSON file

import requests

url = "http://198.18.134.28:8080/api/running/vpn"
user = 'admin'
password = 'admin'
payload = open('newVPN.json', 'rb').read()
headers = {
    'content-type': "application/vnd.yang.data+json",
    }

response = requests.request("POST", url, data=payload, headers=headers, auth=(user, password))

print("Telstra VPN Created")
