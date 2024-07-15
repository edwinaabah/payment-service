from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

payments = []

ORDER_SERVICE_URL = "http://order_service:5002/orders"

@app.route('/payments', methods=['POST'])
def create_payment():
    data = request.json
    order_id = data.get('order_id')
    amount = data.get('amount')
    
    if not order_id or not amount:
        return jsonify({"error": "Invalid data"}), 400
    
    order_response = requests.get(f"{ORDER_SERVICE_URL}/{order_id}")
    if order_response.status_code == 200:
        order = order_response.json()
        payment = {"order_id": order_id, "amount": amount, "order": order}
        payments.append(payment)
        return jsonify(payment), 201
    else:
        return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
