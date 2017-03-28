from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/")
def dark():
    return render_template('index-dark.html')


# @app.route("/L3VpnDeploy/")
# def L3VpnDeploy():
#    return render_template('Backup/L3VpnDeploy.html')

if __name__ == "__main__":
    app.run()
