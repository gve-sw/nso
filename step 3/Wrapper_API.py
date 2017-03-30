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

class Wrapper_API(object):
    """
    This class is used to interact with the NSO API
    """
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.headers = {'Content-Type': 'application/vnd.yang.data+json',
                        'Accept': 'application/vnd.yang.data+json'}

    def getDevices(self):
        """
        Retrieves a list of devices from the NSO API
        """
        devicesURL = 'running/devices'
        url = 'http://' + self.host + '/api' + '/' + devicesURL

        response = requests.get(url, auth=(self.username, self.password),
                                headers=self.headers, verify=False)
        return response

    def getTopology(self):
        """
        Retrieves a list of devices and their relationships in a topology from the NSO API
        """
        TopologyURL = 'running/topology'

        url = 'http://' + self.host + '/api' + '/' + TopologyURL

        response = requests.get(url, auth=(self.username, self.password),
                                headers=self.headers, verify=False)
        return response

    def getSnmpConfig(self):
        """
        Retrieves SNMP config from the NSO API
        """
        snmpConfigURL = 'running/snmp'

        url = 'http://' + self.host + '/api' + '/' + snmpConfigURL

        response = requests.get(url, auth=(self.username, self.password),
                                headers=self.headers, verify=False)
        return response

    def createVPN(self, outfile):
        """
        Creates a VPN through the NSO API
        """
        vpnData = json.dumps(outfile)
        vpnURL = 'running/vpn'
        url = 'http://' + self.host + '/api' + '/' + vpnURL

        response = requests.request("POST", url, data=vpnData, headers=self.headers, auth=(self.username, self.password), verify=False)

        print(response.text)

    def deleteVPN(self, name):
        """
        Deletes the specified VPN through the NSO API
        """

        url = 'http://' + self.host + '/api/running/vpn/l3vpn' + '/' + name

        response = requests.request("DELETE", url, headers=self.headers, auth=(self.username, self.password), verify=False)

        print (response.text)