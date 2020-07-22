from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "item1",
                "price": 100
            }
        ]
    }
]
#index page
@app.route('/')
def home():
    return "Welcome to my store"

#POST http://127.0.01:5000/store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET http://127.0.0.1:5000/store
@app.route('/store')
def get_stores():
    return jsonify({'stores' : stores})

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'messege': 'store not found'})

@app.route('/store/<string:name>/item', methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price'] 
            }

            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'messege': 'store not found'})


@app.route('/store/<string:name>/item')
def get_items_from_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({"items": store['items']})

app.run(port=5000)


