from flask import Flask, render_template
# import pymysql

app = Flask(__name__)

# 查询数据库中的数据
@app.route("/")
def index():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")