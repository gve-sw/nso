from flask import Flask, render_template, request, redirect
from collections import OrderedDict
from Wrapper_API import Wrapper_API
import json

host = '198.18.134.28:8080'
username = "admin"
password = "admin"


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index-dark.html')


@app.route("/L3VpnDeploy")
def L3VpnDeploy():
    return render_template('L3VpnDeploy.html')

@app.route("/deleteVPN")
def deleteVPN():
    return render_template('deleteVPN.html')

@app.route("/deleteVPN", methods= ['POST'])
def removeVPN():
    name = request.form['vpnDelete']
    print (name)
    apiRequest = Wrapper_API(host, username, password)
    apiRequest.deleteVPN(name)
    return redirect('/')

@app.route("/L3VpnDeploy", methods = ['POST'])
def createJSON():
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
    ''' % {'vpnName': request.form['name'],
           'routeDistinguisher': request.form['route_distinguisher'],
           'sourceID': request.form['Source_ID'],
           'sourceCeDevice': request.form['Source_Device'],
           'sourceCeInterface': request.form['Source_Interface'],
           'sourceNetwork': request.form['Source_Network'],
           'sourceBandwidth': request.form['Source_Bandwidth'],
           'sourceAsNumber': request.form['Source_AS_Number'],
           'destinationID': request.form['Destination_ID'],
           'destinationCeDevice': request.form['Destination_Device'],
           'destinationCeInterface': request.form['Destination_Interface'],
           'destinationNetwork': request.form['Destination_Network'],
           'destinationBandwidth': request.form['Destination_Bandwidth'],
           'destinationAsNumber': request.form['Destination_AS_Number']
           }

    data_formatted = json.loads(data, object_pairs_hook=OrderedDict)
    apiRequest = Wrapper_API(host, username, password)
    apiRequest.createVPN(data_formatted)

    return redirect('/')

if __name__ == "__main__":
    app.run()
