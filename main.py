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
    cursor.execute("DELETE FROM Farmers WHERE farmer_id = %s", (farmer_id))
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


# ===== ROOT =====
@app.route("/")
def home():
    return """
    <h1>Agri Management</h1>
    <ul>
        <li><a href='/farmers'>Farmers</a></li>
        <li><a href='/crops'>Crops</a></li>
        <li><a href='/markets'>Markets</a></li>
    </ul>
    """


if __name__ == "__main__":
    app.run(debug=True, port=5000)
