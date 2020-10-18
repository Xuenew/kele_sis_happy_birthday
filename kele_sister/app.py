from flask import Flask

app = Flask(__name__)


@app.route('/kele_sis')
def hello_world():
    return '你好呀 可乐妹妹！！！'


if __name__ == '__main__':
    app.run(host="0.0.0.0")
