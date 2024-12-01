from flask import Flask, render_template, redirect, url_for, session
from flask_oidc import OpenIDConnect
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
oidc = OpenIDConnect(app)

@app.route('/')
def index():
    if oidc.user_loggedin:
        return redirect(url_for('profile'))
    return render_template('index.html')

@app.route('/login')
@oidc.require_login
def login():
    user_info = oidc.user_getinfo(["name", "email", "picture"])
    session["user"] = user_info
    return redirect(url_for('profile'))

# @app.route("/user_info")
# @oidc.require_login
# def user_info():
#     user = session.get("user")
#     if not user:
#         return redirect(url_for("index"))  # Redirect if user info is not available
#     return render_template("user_info.html", user=user)

@app.route('/logout')
def logout():
    oidc.logout()
    session.clear()
    return redirect(url_for('index'))

@app.route('/profile')
@oidc.require_login
def profile():
    user_info = oidc.user_getinfo(['email', 'name', 'picture'])
    session["user"] = user_info
    return render_template('user_info.html', user=user_info)

if __name__ == '__main__':
    app.run(debug=True)
