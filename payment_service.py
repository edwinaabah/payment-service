from flask import Flask

app = Flask(__name__)

@app.route('/payment')
def payment():
    return "You can make your payment here"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
