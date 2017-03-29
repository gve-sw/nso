from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index-dark.html')


@app.route("/L3VpnDeploy")
def L3VpnDeploy():
    return render_template('L3VpnDeploy.html')

@app.route("/L3VpnDeploy. methods ['POST]")
def createJSON():
    newVPN = request.form["JSON"]
    json dumps
    send api request
    json delete
    print(newVPN)
    return redirect('/')

if __name__ == "__main__":
    app.run()
