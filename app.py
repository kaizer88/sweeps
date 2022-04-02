from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "flask Docker"

@app.route('/api')
def get_data():
    import requests
    email ='ltmagwentshu@gmail.com'
    url = "https://api.apilayer.com/email_verification/{}".format(email)

    payload = {}
    headers= {
      "apikey": "A9n0bzeCjWgEavZsKnfh23yBxqpyFaIn"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text
    return result

@app.route('/add/a=<a>,b=<b>', methods=['GET', 'POST'])
def math_add(a=3, b=4):
    s = a+b
    return s

@app.route('/prod')
def math_prod(a, b):
    return a*b

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
