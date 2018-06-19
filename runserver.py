# 启动文件
from ccms import app


@app.route("/")
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)

