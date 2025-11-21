from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "securekey123"   # Change in production

# User data (in-memory)
users = {
    "nikki": {"pin": "1234", "balance": 5000},
    "admin": {"pin": "0000", "balance": 10000}
}


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].lower()
        pin = request.form["pin"]

        if username in users and users[username]["pin"] == pin:
            session["user"] = username
            return redirect("/menu")
        else:
            return render_template("login.html", error="Invalid username or PIN")

    return render_template("login.html")


@app.route("/menu")
def menu():
    if "user" not in session:
        return redirect("/")
    return render_template("menu.html", user=session["user"])


@app.route("/balance")
def balance():
    if "user" not in session:
        return redirect("/")
    user = session["user"]
    return render_template("balance.html", balance=users[user]["balance"])


@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if "user" not in session:
        return redirect("/")
    user = session["user"]

    if request.method == "POST":
        amount = int(request.form["amount"])
        users[user]["balance"] += amount
        return redirect("/balance")

    return render_template("deposit.html")


@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if "user" not in session:
        return redirect("/")
    user = session["user"]

    if request.method == "POST":
        amount = int(request.form["amount"])
        if amount <= users[user]["balance"]:
            users[user]["balance"] -= amount
            return redirect("/balance")
        else:
            return render_template("withdraw.html", error="Insufficient balance")

    return render_template("withdraw.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
