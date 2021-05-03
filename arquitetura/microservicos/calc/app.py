from flask import Flask
app = Flask(__name__)

@app.route("/calc", methods=["GET"])
def calc():
    res = {}
    res['resultado'] = "calc está funcionando! Versão 1.0"
    return res, 200

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
