from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    return render_template_string("""
        <form method="post">
            <input type="submit" value="Login">
        </form>
    """)

@app.route("/dashboard")
def dashboard():
    return "Dashboard"
