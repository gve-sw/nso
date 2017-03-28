#
#   Cisco Network Services Orchestrator(NSO) Wrapper API
#       v.01
#
#   Joel Fernandez(joelfern@cisco.com)
#       Feb 2017
#
#       This class provides methods to facilitates
#       access to the Network Services Orchestrator API.
#
#   REQUIREMENTS:
#       Python requests library (issue the 'pip install requests' command in shell or cmd)
#
#   WARNING:
#       This script is meant for educational purposes only.
#       Any use of these scripts and tools is at
#       your own risk. There is no guarantee that
#       they have been through thorough testing in a
#       comparable environment and we are not
#       responsible for any damage or data loss
#       incurred with their use.
#
#   INFORMATION:
#       If you have further questions about this API and script, please contact GVE. Here are the contact details:
#           For internal Cisco gve-programmability@cisco.com
#           For Cisco partners, open a case at www.cisco.com/go/ph

import requests
import json
import requests
from collections import OrderedDict

host = '198.18.134.28:8080'
username = 'admin'
password = 'admin'

class Wrapper_API(object):
    """
    This class is used to interact with the NSO API
    """
    def __init__(self):
        self.host = host
        self.username = username
        self.password = password

    def send_api_request(self, phrase):
        """
        Sends a request to the API for retrieving data.
        """
        url = 'http://' + host + '/api' + '/' + phrase
        headers = {'Content-Type': 'application/vnd.yang.data+json',
                   'Accept': 'application/vnd.yang.data+json'}
        response = requests.get(url, auth=(username, password),
                                headers=headers, verify=False)
        return response.text

    def getDevices(self):
        """
        Retrieves a list of devices from the NSO API
        """
        devicesURL = 'running/devices'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(devicesURL)
        return apiResponse

    def getTopology(self):
        """
        Retrieves a list of devices and their relationships in a topology from the NSO API
        """
        TopologyURL = 'running/topology'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(TopologyURL)
        return apiResponse

    def getSnmpConfig(self):
        """
        Retrieves SNMP config from the NSO API
        """
        snmpConfigURL = 'running/snmp'
        apiRequest = Wrapper_API()
        apiResponse = apiRequest.send_api_request(snmpConfigURL)
        return apiResponse

    def createVPN(self):
        data = '''
            {
              "l3vpn:l3vpn": {
                "name": "%(vpnName)s",
                "route-distinguisher": %(routeDistinguisher)s,
                "endpoint": [
                  {
                    "id": "%(sourceID)s",
                    "ce-device": "%(sourceCeDevice)s",
                    "ce-interface": "%(sourceCeInterface)s",
                    "ip-network": "%(sourceNetwork)s",
                    "bandwidth": %(sourceBandwidth)s,
                    "as-number": %(sourceAsNumber)s
                  },
                  {
                    "id": "%(destinationID)s",
                    "ce-device": "%(destinationCeDevice)s",
                    "ce-interface": "%(destinationCeInterface)s",
                    "ip-network": "%(destinationNetwork)s",
                    "bandwidth": %(destinationBandwidth)s,
                    "as-number": %(destinationAsNumber)s
                  }
                ]
              }
            }
        ''' % {'vpnName': input("VPN Name: "),
               'routeDistinguisher': int(input("Route Distinguiser: ")),
               'sourceID': input("ID: "),
               'sourceCeDevice': input("CE Device: "),
               'sourceCeInterface': input("CE Interface: "),
               'sourceNetwork': input("Network Address: "),
               'sourceBandwidth': int(input("Bandwidth: ")),
               'sourceAsNumber': int(input("AS Number: ")),
               'destinationID': input("ID: "),
               'destinationCeDevice': input("CE Device: "),
               'destinationCeInterface': input("CE Interface: "),
               'destinationNetwork': input("Network Address: "),
               'destinationBandwidth': int(input("Bandwidth: ")),
               'destinationAsNumber': int(input("AS Number: "))
               }

        data_formatted = json.loads(data, object_pairs_hook=OrderedDict)

        with open('createVPN.json', 'w') as outfile:
            json.dump(data_formatted, outfile, indent=2)

        payload = open('createVPN.json', 'rb').read()
        response = requests.request("POST", url, data=payload, headers=headers, auth=(user, password))

        print()
        print(response.text)
        print("VPN Created")