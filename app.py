from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "flask Docker"


@app.route('/api')
def get_data():

    # if key doesn't exist, returns None
    email = request.args.get('email')
    url = "https://api.apilayer.com/email_verification/{}".format(email)

    payload = {}
    headers = {
        "apikey": "A9n0bzeCjWgEavZsKnfh23yBxqpyFaIn"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return jsonify(response.text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
