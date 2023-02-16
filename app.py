from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/plama.db"
db = SQLAlchemy(app)


@app.route('/')
def index():
    """Show a list of products"""
    return render_template("index.html")

@app.route('/register')
def register():
    """Register user"""
    if request.method == "POST":
        return redirect("/")
    else:
        return render_template("register.html")

@app.route('/login')
def login():
    """Login user"""
    if request.method == "POST":
        return redirect("/")
    else:
        return render_template("login.html")

@app.route('/sell')
def sell():
    """Sell products"""
    if request.method == "POST":
        return redirect("/")
    else:
        return render_template("sell.html")

@app.route('/edit')
def edit():
    """Edit a list of user's products"""
    if request.method == "POST":
        return redirect("/edit")
    else:
        return render_template("edit.html")

if __name__ == "__main__":
    app.run()