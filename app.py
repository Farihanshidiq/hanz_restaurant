from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Contoh data menu
menu_items = [
    {"id": 1, "name": "Noodles", "price": "Rp23.000", "image": "assets/img/noodle.jpg"},
    {"id": 2, "name": "Chicken", "price": "Rp15.000", "image": "assets/img/chicken.jpg"},
    {"id": 3, "name": "French Fries", "price": "Rp11.000", "image": "assets/img/french_fries.jpg"},
    {"id": 4, "name": "Pizza", "price": "Rp50.000", "image": "assets/img/pizza.jpg"},
    {"id": 5, "name": "Burger", "price": "Rp30.000", "image": "assets/img/burger.jpg"},
    {"id": 6, "name": "Salad", "price": "Rp20.000", "image": "assets/img/salad.jpg"},
]

# Endpoint untuk mendapatkan semua item menu
@app.route('/api/menu', methods=['GET'])
def get_menu():
    return jsonify(menu_items)

# Endpoint untuk mendapatkan item menu berdasarkan ID
@app.route('/api/menu/<int:item_id>', methods=['GET'])
def get_menu_item(item_id):
    item = next((item for item in menu_items if item["id"] == item_id), None)
    return jsonify(item) if item else ('', 404)

# Endpoint untuk menambahkan item menu baru
@app.route('/api/menu', methods=['POST'])
def add_menu_item():
    new_item = request.get_json()
    new_item["id"] = len(menu_items) + 1
    menu_items.append(new_item)
    return jsonify(new_item), 201

# Endpoint untuk memperbarui item menu berdasarkan ID
@app.route('/api/menu/<int:item_id>', methods=['PUT'])
def update_menu_item(item_id):
    item = next((item for item in menu_items if item["id"] == item_id), None)
    if not item:
        return ('', 404)
    
    updated_data = request.get_json()
    item.update(updated_data)
    return jsonify(item)

# Endpoint untuk menghapus item menu berdasarkan ID
@app.route('/api/menu/<int:item_id>', methods=['DELETE'])
def delete_menu_item(item_id):
    global menu_items
    menu_items = [item for item in menu_items if item["id"] != item_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
