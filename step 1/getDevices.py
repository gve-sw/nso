# Script receives a list of devices currently configured under NSO.

import requests

host = '198.18.134.28:8080'
username = 'admin'
password = 'admin'

def getDevices(host, username, password):
    """
    Sends a request to the API for retrieving data
    """
    url = 'http://' + host + '/api/running/devices'
    headers = {
        'Content-Type': 'application/vnd.yang.data+json'
        }
    response = requests.get(url, auth=(username, password),
                                headers=headers, verify=False)

    return response.text

if __name__ == '__main__':
    print(getDevices(host, username, password))
