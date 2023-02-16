from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://///home/sosuke/CODEGYM_FinalProject/plama/db/plama.db"
db = SQLAlchemy(app)

# class user(db.Model):
#     __tablename__ = "user"
#     id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
#     name = Column(Text, nullable=False)
#     room_number = Column(Text, nullable=False)
#     hash = Column(VARCHAR, nullable=False)



# class product(db.Model):
#     __tablename__ = 'product'
#     id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
#     user_id  = Column(Integer, ForeignKey("user.id", nullable=False))
#     title = Column(Text, nullable=False)
#     body  = Column(Text, nullable=False)
#     picture_path  = Column(Text, nullable=False)
#     date = Column(DateTime, default=datetime.now(), nullable=False)


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