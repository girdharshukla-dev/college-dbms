from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = db.cursor(dictionary=True)

## farmers
@app.route("/farmers")
def list_farmers():
    cursor.execute("SELECT * FROM Farmers")
    farmers = cursor.fetchall()
    return render_template("farmers.html", farmers=farmers)

@app.route("/farmers/add", methods=["POST"])
def add_farmer():
    name = request.form["farmer_name"]
    village = request.form.get("village", "")
    phone = request.form.get("phone", "")
    cursor.execute(
        "INSERT INTO Farmers (farmer_name, village, phone) VALUES (%s, %s, %s)",
        (name, village, phone)
    )
    db.commit()
    return redirect(url_for("list_farmers"))

@app.route("/farmers/delete/<int:farmer_id>")
def delete_farmer(farmer_id):
    cursor.execute("DELETE FROM Farmers WHERE farmer_id = %s", (farmer_id,))
    db.commit()
    return redirect(url_for("list_farmers"))

@app.route("/farmers/update", methods=["POST"])
def update_farmer( ):
    farmer_id = request.form["farmer_id"]
    name = request.form["farmer_name"]
    village = request.form.get("village","")
    phone = request.form.get("phone","")
    cursor.execute(
        "UPDATE Farmers SET farmer_name=%s, village=%s, phone=%s WHERE farmer_id=%s",
        (name, village, phone, farmer_id)
    )
    db.commit()
    return redirect(url_for("list_farmers"))  

## crops
@app.route("/crops")
def list_crops():
    cursor.execute("SELECT * FROM Crops")
    crops = cursor.fetchall()
    return render_template("crops.html", crops=crops)

@app.route("/crops/add", methods=["POST"])
def add_crop():
    name = request.form["crop_name"]
    season = request.form.get("season", "")
    cursor.execute(
        "INSERT INTO Crops (crop_name, season) VALUES (%s, %s)",
        (name, season)
    )
    db.commit()
    return redirect(url_for("list_crops"))

@app.route("/crops/delete/<int:crop_id>")
def delete_crop(crop_id):
    cursor.execute("DELETE FROM Crops WHERE crop_id = %s", (crop_id,))
    db.commit()
    return redirect(url_for("list_crops"))

@app.route("/crops/update", methods=["POST"])
def update_crop():
    crop_id = request.form["crop_id"]
    name = request.form["crop_name"]
    season = request.form.get("season", "")
    cursor.execute(
        "UPDATE Crops SET crop_name=%s, season=%s WHERE crop_id=%s",
        (name, season, crop_id)
    )
    db.commit()
    return redirect(url_for("list_crops"))

## markets
@app.route("/markets")
def list_markets():
    cursor.execute("SELECT * FROM Markets")
    markets = cursor.fetchall()
    return render_template("markets.html", markets=markets)

@app.route("/markets/add", methods=["POST"])
def add_market():
    name = request.form["market_name"]
    location = request.form.get("location", "")
    cursor.execute(
        "INSERT INTO Markets (market_name, location) VALUES (%s, %s)",
        (name, location)
    )
    db.commit()
    return redirect(url_for("list_markets"))

@app.route("/markets/delete/<int:market_id>")
def delete_market(market_id):
    cursor.execute("DELETE FROM Markets WHERE market_id = %s", (market_id,))
    db.commit()
    return redirect(url_for("list_markets"))

@app.route("/markets/update", methods=["POST"])
def update_market():
    market_id = request.form["market_id"]
    name = request.form["market_name"]
    location = request.form.get("location", "")
    cursor.execute(
        "UPDATE Markets SET market_name=%s, location=%s WHERE market_id=%s",
        (name, location, market_id)
    )
    db.commit()
    return redirect(url_for("list_markets"))


## transactions
## transactions
@app.route("/transactions")
def list_transactions():
    cursor.execute("SELECT * FROM Transactions")
    transactions = cursor.fetchall()
    return render_template("transactions.html", transactions=transactions)

@app.route("/transactions/add", methods=["POST"])
def add_transaction():
    farmer_id = request.form["farmer_id"]
    crop_id = request.form["crop_id"]
    market_id = request.form["market_id"]
    quantity = request.form["quantity"]
    price = request.form["price"]
    cursor.execute(
        "INSERT INTO Transactions (farmer_id, crop_id, market_id, quantity, price) VALUES (%s, %s, %s, %s, %s)",
        (farmer_id, crop_id, market_id, quantity, price)
    )
    db.commit()
    return redirect(url_for("list_transactions"))

@app.route("/transactions/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    cursor.execute("DELETE FROM Transactions WHERE transaction_id = %s", (transaction_id,))
    db.commit()
    return redirect(url_for("list_transactions"))

@app.route("/transactions/update", methods=["POST"])
def update_transaction():
    transaction_id = request.form["transaction_id"]
    farmer_id = request.form["farmer_id"]
    crop_id = request.form["crop_id"]
    market_id = request.form["market_id"]
    quantity = request.form["quantity"]
    price = request.form["price"]
    cursor.execute(
        "UPDATE Transactions SET farmer_id=%s, crop_id=%s, market_id=%s, quantity=%s, price=%s WHERE transaction_id=%s",
        (farmer_id, crop_id, market_id, quantity, price, transaction_id)
    )
    db.commit()
    return redirect(url_for("list_transactions"))


# ===== ROOT =====
@app.route("/")
def home():
    return """
    <h1>Agri Management</h1>
    <ul>
        <li><a href='/farmers'>Farmers</a></li>
        <li><a href='/crops'>Crops</a></li>
        <li><a href='/markets'>Markets</a></li>
        <li><a href='/transactions'>Transactions</a></li>
    </ul>
    """


if __name__ == "__main__":
    app.run(debug=True, port=5000)
