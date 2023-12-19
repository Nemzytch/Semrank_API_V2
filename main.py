from flask import Flask
app = Flask(__name__)
import requests


@app.route('/')
def hello_world():
    return 'Hellooooooaaaaa, Worldo!'

@app.route('/test')
def test():
    return requests.get('http:example.com').text





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
