# Retrieves a list of the devices in the topology and their links configured in NSO.

import requests

host = '198.18.134.28:8080'
username = 'admin'
password = 'admin'

def getTopology(host, username, password):
    """
    Sends a request to the API for retrieving data
    """
    url = 'http://' + host + '/api/running/topology'
    headers = {
        'Content-Type': 'application/vnd.yang.data+json'
        }
    response = requests.get(url, auth=(username, password),
                                headers=headers, verify=False)

    return response.text

if __name__ == '__main__':
    print(getTopology(host, username, password))