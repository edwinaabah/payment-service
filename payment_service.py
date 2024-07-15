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
    
    # Process payment logic here if needed
    payment = {"order_id": order_id, "amount": amount}
    payments.append(payment)
    
    return jsonify(payment), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
