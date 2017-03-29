import json
from collections import OrderedDict
from Wrapper_API import Wrapper_API

host = "http://198.18.134.28:8080/api/running/vpn"
username = 'admin'
password = 'admin'
headers = {
        'content-type': "application/vnd.yang.data+json",
        }

def main():
    """
    Main method to start this L3VPN deployment tool.
    """

    print("######################################################")
    print("####                                              ####")
    print("####  NSO L3VPN Deployment Tool                   ####")
    print("####                                              ####")
    print("####  Developer: Joel Fernandez, Ajay Doshi       ####")
    print("####  Email: joelfern@cisco.com                   ####")
    print("####                                              ####")
    print("######################################################")
    print()
    print("This tool uses the nourthbound NSO API to deploy L3VPNs")
    print()

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

    apiRequest = Wrapper_API(host, username, password)
    apiRequest.createVPN(payload)

    print()
    print(apiRequest.text)
    print("VPN Created")


if __name__ == "__main__":
    main()
