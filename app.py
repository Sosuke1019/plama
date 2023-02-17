from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from models.models import user


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
    user_id = session["user_id"]

    users = user.query.all()
    return render_template("index.html", users=users)

@app.route('/login')
def login():
    """Login user"""

    #sessionをクリアする
    session.clear()

    if request.method == "POST":

        #取得した行のidをsessionの中に保存する


        return redirect("/")
    else:
        return render_template("login.html")

@app.route('/logut')
def logout():
    """Log user out"""

    #sessionをクリアする
    session.clear()

    return redirect("/")


# @app.route('/register')
# def register():
#     """Register user"""
#     if request.method == "POST":
#         return redirect("/")
#     else:
#         return render_template("register.html")
    

# @app.route('/sell')
# def sell():
#     """Sell products"""
#     if request.method == "POST":
#         return redirect("/")
#     else:
#         return render_template("sell.html")

# @app.route('/edit')
# def edit():
#     """Edit a list of user's products"""
#     if request.method == "POST":
#         return redirect("/edit")
#     else:
#         return render_template("edit.html")

# if __name__ == "__main__":
#     app.run()