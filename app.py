from flask import Flask, request, redirect, url_for, session, render_template_string

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Dummy User
USER = {
    "email": "admin@test.de",
    "password": "1234"
}

# HTML direkt aus Dateien laden
def load_html(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

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

    return render_template_string(load_html("login.html"))

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    html = load_html("dashboard.html")
    return render_template_string(html, user=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
