from flask import Flask, jsonify,render_template_string, request

app = Flask(__name__)

customer_name = {
    "Brian Keyo":      {"KES": 50000},
    "Mallory Odongo":  {"KES": 21000},
    "Keith Ken":       {"KES": 39192},
    "Jayden Okoth":    {"KES": 48342},
    "Stephen Mei":     {"KES": 10100}
}

# HTML template for the home route
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eldoret Hardware</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 500px; margin: 50px auto; padding: 20px; }
        input[type="text"] { padding: 8px; width: 70%; font-size: 16px; }
        button { padding: 8px 15px; font-size: 16px; cursor: pointer; }
        #result { margin-top: 20px; font-weight: bold; font-size: 18px; }
    </style>
</head>
<body>
    <h1>Eldoret Hardware</h1>
    <p>Enter a customer's name to check their credit balance:</p>
    
    <form id="searchForm" action="/api/balance" method="get">
        <input type="text" id="customerInput" name="name" placeholder="e.g., Brian Keyo" required>
        <button type="submit">Check Balance</button>
    </form>

    <div id="result"></div>

    <script>
        document.getElementById('searchForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const name = document.getElementById('customerInput').value;
            const response = await fetch(`/api/balance?name=${encodeURIComponent(name)}`);
            const data = await response.json();
            
            const resultDiv = document.getElementById('result');
            if (response.ok) {
                resultDiv.style.color = 'green';
                resultDiv.textContent = `${data.customer}: KES ${data.balance.toLocaleString()}`;
            } else {
                resultDiv.style.color = 'red';
                resultDiv.textContent = data.error;
            }
        });
    </script>
</body>
</html>
"""
# 1. Home route (/) returning the HTML page with the shop name and search form
@app.route("/")
def home():
  return render_template_string(HTML_TEMPLATE)


# 2. Required API route (/api/balance) accepting a customer name query parameter
@app.route("/api/balance", methods=["GET"])
def get_balance():
  name = request.args.get("name", "").strip()

  if not name:
    return jsonify({"error": "Please provide a customer name."}), 400

  # Search case-insensitively through your dictionary keys
  for customer, details in customer_name.items():
    if customer.lower() == name.lower():
      return jsonify({"customer": customer, "balance": details["KES"]})

  return jsonify({"error": f"Customer '{name}' not found."}), 404


# 3. Your existing route (/debtors) to view all customers at once
@app.route("/debtors", methods=["GET"])
def get_debtors():
  return jsonify(customer_name)


if __name__ == "__main__":
  app.run(debug=True)