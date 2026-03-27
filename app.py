from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Dummy User (später DB)
USER = {
    "email": "admin@test.de",
    "password": "1234"
}

@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == USER["email"] and password == USER["password"]:
            session["user"] = email
            return redirect(url_for("dashboard"))
        else:
            return "Login fehlgeschlagen"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", user=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
