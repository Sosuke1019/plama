import os
from flask import Flask, flash, redirect, render_template, request
from flask_session import Session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from models.models import user, product
from models.database import db_session
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import base64


# 画像のアップロード先のディレクトリ
UPLOAD_FOLDER = '/static/images'
# アップロードされる拡張子の制限
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models/plama.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#16MBまでのfileをアップロード出来る
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# falsk-loginとFlaskアプリを紐づける
login_manager = LoginManager()
login_manager.init_app(app)

# セッション情報を暗号化するためのキー
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

    def image_file_to_base64(encoded_picture_path):
        return encoded_picture_path.decode('utf-8')
    
    products = product.query.all()

    # 出品された商品が無かった場合の処理
    if not products:
        return render_template("index.html")

    # productテーブルのuser_idに一致するuserテーブルのレコードのnameとroom_numberを取ってくる
    # productの個数分の要素(productに対応した名前)が入ったリストを取り出す。
    # user_name = db_session.query(user).join(product, product.user_id == user.id).all()
    def search_user(product_user_id):
        return user.query.filter_by(id=product_user_id).first()
    
    # productテーブルのuser_idに一致するuserテーブルのレコードのnameとroom_numberを取ってきたい。.nameで名前を返す。※nameを一発で取ってこれるならそれでもいい。
    # SELECT name FROM user WHERE id = (SELECT user_id FROM product);
    # User = user.query.filter_by(room_number=room_number).first()

    return render_template("index.html", products=products, image_file_to_base64=image_file_to_base64, search_user=search_user)
    

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
    

@app.route('/sell', methods=["GET", "POST"])
@login_required
def sell():
    """Sell products"""
    if request.method == "POST":
        # .と拡張子の確認
        def allowed_file(filename):
            return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
        
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template("error.html", message="no file page")

        # fileが選択されていなかった場合はエラーページをリターンする
        file = request.files['file']
        if file.filename == '':
            return render_template("error.html", message="no selected file")
        
        # base64フォーマットにencodeする
        if file and allowed_file(file.filename):
            img_base64 = base64.b64encode(file.read())

        # 商品名が空白の場合はエラーページをリターンする
        title = request.form.get("title")
        if not title:
            return render_template("error.html", message="missing title")

        # 説明文が空白の場合はエラーページをリターンする
        body = request.form.get("body")
        if not body:
            return render_template("error.html", message="missing explanation")
        
        # アップロード時の日付と時刻を取得
        date = datetime.date.today()
        
        # base64フォーマットをDBに保存
        Product = product(user_id=current_user.id, title=title, body=body, picture_path=img_base64, date=date)
        db_session.add(Product)
        db_session.commit()

        flash("Success")

        return redirect("/")
    else:
        return render_template("sell.html")

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