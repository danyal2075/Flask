from flask import Flask, render_template, jsonify, request


app = Flask(__name__)
store = [
    {
        'name':'beautiful store',
        'items': [
            {
                'name':'flower',
                'price': '100'
            }
        ]
    },
    {
        'name':'beautiful store 2 ',
        'items': [
            {
                'name':'flower',
                'price': '100'
            }
        ]
    }
]

@app.route('/')
def home():
    return 'Hello API'

@app.route('/store', methods = ['POST'])
def create_store():
    datarequest = request.get_json()
    new_store = {
        'name': datarequest,
        'items': []
    }
    store.append(new_store)

    return jsonify(new_store)

@app.route('/store')
def all_store_data():
    return jsonify(store)   

@app.route('/store/<string:name>')
def get_store_name(name):
    for stores in store:
        if(stores['name'] == name):
            return jsonify(stores)
    return jsonify({'message': 'Store not found'})
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for stores in store:
        if(stores['name'] == name):
            new_item = {
                'name':request_data['name'],
                'price': request_data['price']
            }
            stores['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})



if __name__ == '__main__':
    app.run(debug=True)