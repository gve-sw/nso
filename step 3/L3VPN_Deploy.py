from Wrapper_API import Wrapper_API


host = '198.18.134.28:8080'
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
    print("This tool uses the northbound NSO API to deploy L3VPNs")
    print()

    api = Wrapper_API(host, username, password)
    vpn = api.createVPN()


if __name__ == "__main__":
    main()
