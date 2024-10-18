from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/sub", methods=["GET"])
def sub():
    res = {}
    op1 = request.args.get('op1')
    op2 = request.args.get('op2')

    if not op1 or not op2:
        res['resultado'] = "op1 ou op2 não informado"
        return res, 400
    
    res['resultado'] = float(op1) - float(op2)
    return res, 200

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
