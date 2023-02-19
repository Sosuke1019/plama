from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from models.models import user
import sqlite3

#DBに接続
conn = sqlite3.connect('models/plama.db',isolation_level=None, check_same_thread=False)
db = conn.cursor()


app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    """Show a list of products"""
    # user_id = session["user_id"]

    users = user.query.all()
    return render_template("index.html", users=users)

# @app.route('/login', methods=["GET", "POST"])
# def login():
#     """Login user"""

#     #sessionをクリアする
#     session.clear()

#     if request.method == "POST":

#         #取得した行のidをsessionの中に保存する


#         return redirect("/")
#     else:
#         return render_template("login.html")

# @app.route('/logut')
# def logout():
#     """Log user out"""

#     #sessionをクリアする
#     session.clear()

#     return redirect("/")


@app.route('/register', methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        #ユーザー名が空白の場合はミスをリターンする
        username = request.form.get("username")
        if not request.form.get("username"):
            return render_template("error.html", message="missing name")

        #ユーザー名が既に存在する場合はミスをリターンする
        db.execute("SELECT * FROM user WHERE name = ?", (username,))
        rows = db.fetchone()
        conn.close()
        if rows is not None:
            return render_template("error.html", message="invalid username")

        #部屋番号が空白/既に存在する場合はミスをリターンする
        # room_number = request.form.get("room_numbrer")

        #パスワードが空白の場合はミスをリターンする

        #passwordとconfirmationのパスワードが異なる場合はミスをリターンする

        #パスワードをハッシュ化する

        #新しいユーザ・部屋番号・ハッシュをuserにINSERTする

        #取得した行のidをsessionの中に保存する

        flash("Registered")
        
        return redirect("/")
    else:
        return render_template("register.html")
    

# @app.route('/sell', methods=["GET", "POST"])
# def sell():
#     """Sell products"""
#     if request.method == "POST":
#         return redirect("/")
#     else:
#         return render_template("sell.html")

# @app.route('/edit', methods=["GET", "POST"])
# def edit():
#     """Edit a list of user's products"""
#     if request.method == "POST":
#         return redirect("/edit")
#     else:
#         return render_template("edit.html")


if __name__ == "__main__":
    app.run()