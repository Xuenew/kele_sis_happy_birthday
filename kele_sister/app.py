from flask import Flask
from flask import render_template
from flask import send_file
# app = Flask(__name__,template_folder='../templates',static_folder="../static",)
app = Flask(__name__,template_folder=".")
""",
            template_folder='/templates',
            static_folder=']/static',"""

@app.route('/kele_sis')
def hello_world():
    return render_template("./index.html")
    # return '你好呀 可乐妹妹！！！'


if __name__ == '__main__':
    # 本地调用的时候可以这样
    app.run(host="0.0.0.0")

