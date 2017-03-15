# Script deletes the previously created VPN for the customer called Telstra.

import requests

url = "http://198.18.134.28:8080/api/running/vpn/l3vpn/Telstra"
user = 'admin'
password = 'admin'

headers = {
    'content-type': "application/vnd.yang.data+json",
    }

response = requests.request("DELETE", url, headers=headers, auth=(user, password))

print("Telstra VPN Deleted")
