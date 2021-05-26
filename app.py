from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)

PORT = 3200
HOST = '0.0.0.0'

@app.route('/')
def home():
    return "<h1 style='color:green'>Hello Flask.</h1>"

if __name__ == '__main__':
    print("Server Running at Port %s"%(PORT))
    app.run(host=HOST, port=PORT)