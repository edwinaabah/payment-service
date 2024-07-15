from flask import Flask, request, jsonify

app = Flask(__name__)

payments = []

@app.route('/payments', methods=['POST'])
def create_payment():
    data = request.json
    order_id = data.get('order_id')
    amount = data.get('amount')
    
    if not order_id or not amount:
        return jsonify({"error": "Invalid data"}), 400
    
    # Fetch order details from order service (if needed)
    # Since you want to be independent of order_service, you may skip this or handle gracefully
    order = {}  # Assuming no order details needed or available
    
    payment = {"order_id": order_id, "amount": amount, "order": order}
    payments.append(payment)
    
    return jsonify(payment), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
