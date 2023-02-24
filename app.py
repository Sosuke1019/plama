import os
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from models.models import user, product
from models.database import db_session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models/plama.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

#falsk-loginとFlaskアプリを紐づける
login_manager = LoginManager()
login_manager.init_app(app)

#セッション情報を暗号化するためのキー
app.secret_key = os.urandom(24)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

#cookieからセッションのチェックを行う
@login_manager.user_loader
def load_user(id):
    return user.query.get(id)

@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login')

@app.route('/')
@login_required
def index():
    """Show a list of products"""

    users = user.query.all()
    return render_template("index.html", users=users)

@app.route('/login', methods=["GET", "POST"])
def login():
    """Login user"""

    if request.method == "POST":

        #ユーザー名が空白の場合はエラーページをリターンする
        username = request.form.get("username")
        if not username:
            return render_template("error.html", message="missing name")
        
        #パスワードが空白の場合はエラーページをリターンする
        password = request.form.get("password")
        if not password:
            return render_template("error.html", message="missing password")
        
        #フォームで送られてきた名前の存在を確認する
        User = user.query.filter_by(name=username).first()
        if User is None:
            return render_template("error.html", message="invalid username")

        #パスワードの確認をする
        if check_password_hash(User.hash, password):
            login_user(User)
            flash("logged in")
            return redirect("/")
        else:
            return render_template("error.html", message="invalid password")
        
    else:
        return render_template("login.html")
    

@app.route('/logout')
@login_required
def logout():
    """Log user out"""

    logout_user()

    return redirect("/login")


@app.route('/register', methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        #ユーザー名が空白の場合はエラーページをリターンする
        username = request.form.get("username")
        if not username:
            return render_template("error.html", message="missing name")

        #ユーザー名が既に存在する場合はエラーページをリターンする
        User = user.query.filter_by(name=username).first()
        if User is not None:
            return render_template("error.html", message="invalid username")

        #部屋番号が空白の場合はエラーページをリターンする
        room_number = request.form.get("room_number")
        if not room_number:
            return render_template("error.html", message="missing room-number")

        #部屋番号が既に存在する場合はエラーページをリターンする
        User = user.query.filter_by(room_number=room_number).first()
        if User is not None:
            return render_template("error.html", message="invalid room-number")

        #パスワードが空白の場合・confiramationと一致しない場合はエラーページをリターンする
        password = request.form.get("password")
        if not password:
            return render_template("error.html", message="missing password")
        elif password != request.form.get("confirmation"):
            return render_template("error.html", message="passwords don't match")

        #パスワードをハッシュ化する
        hash = generate_password_hash(password, method='sha512', salt_length=10000)

        #Userのインスタンスを作成
        User = user(name=username,room_number=room_number,hash=hash)
        db_session.add(User)
        db_session.commit()

        flash("Registered")
        
        return redirect("/")
    else:
        return render_template("register.html")
    

# @app.route('/sell', methods=["GET", "POST"])
# @login_required
# def sell():
#     """Sell products"""
#     if request.method == "POST":
#         return redirect("/")
#     else:
#         return render_template("sell.html")

# @app.route('/edit', methods=["GET", "POST"])
# @login_required
# def edit():
#     """Edit a list of user's products"""
#     if request.method == "POST":
#         return redirect("/edit")
#     else:
#         return render_template("edit.html")


if __name__ == "__main__":
    app.run()