from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    data1 = {'name':'Danyal',
             'age':29}
    
    return jsonify(data1)
if __name__ == '__main__':
    app.run(debug=True)