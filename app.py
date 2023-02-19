import os
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from models.models import user
import sqlite3
from datetime import timedelta
from helpers  import generate_password_hash

#DBに接続
conn = sqlite3.connect('models/plama.db',isolation_level=None, check_same_thread=False)
db = conn.cursor()


app = Flask(__name__)

#セッション情報を暗号化するためのキー
app.secret_key = os.urandom(24)
#セッションの有効時間を設定する
app.permanent_session_lifetime = timedelta(minutes=5)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    """Show a list of products"""
    

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

        #ユーザー名が空白の場合はエラーページをリターンする
        username = request.form.get("username")
        if not username:
            return render_template("error.html", message="missing name")

        #ユーザー名が既に存在する場合はエラーページをリターンする
        db.execute("SELECT * FROM user WHERE name = ?", (username,))
        rows_username_check = db.fetchone()
        if rows_username_check is not None:
            return render_template("error.html", message="invalid username")

        #部屋番号が空白の場合はエラーページをリターンする
        room_number = request.form.get("room_number")
        if not room_number:
            return render_template("error.html", message="missing room-number")

        #部屋番号が既に存在する場合はエラーページをリターンする
        db.execute("SELECT * FROM user WHERE room_number = ?", (room_number,))
        rows_room_number_check = db.fetchone()
        if rows_room_number_check is not None:
            return render_template("error.html", message="invalid room-number")

        #パスワードが空白の場合・confiramationと一致しない場合はエラーページをリターンする
        password = request.form.get("password")
        if not password:
            return render_template("error.html", message="missing password")
        elif password != request.form.get("confirmation"):
            return render_template("error.html", message="passwords don't match")

        #パスワードをハッシュ化する
        hash_password = generate_password_hash(request.form.get("password"))

        #新しいユーザ・部屋番号・ハッシュをuserテーブルにINSERTする
        db.execute("INSERT INTO user (name, room_number, hash) VALUES(?,?,?)", (username, room_number, hash_password))

        #取得した行のidをsessionの中に保存する
        new_user = db.execute("SELECT * FROM user WHERE name = ?", (username,))
        new_user = new_user.fetchone()
        session["user_id"] = new_user[0]

        conn.close()

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