
from flask import Flask, render_template
from flask import request

# 创建Ｆｌａｓｋ的程序实例
app = Flask(__name__)

# ‘/’表示根目录
@app.route('/')
@app.route('/index')
# 路由是为了匹配用户的请求地址，会自动的执行视图函数
# 视图函数
def index():
    return "<h1>欢迎</h1>"

# 给视图函数传参数
@app.route('/login/<name>/<age>')
def login(name, age):
    return "<h1>欢迎登录，%s,%s</h1>" % (name, age)


@app.route('/calcute/<int:n1>/<int:n2>')
def calcute(n1, n2):
    # n1 = int(n1)
    # n2 = int(n2)
    n3 = n1 + n2
    return "%d + %d = %d" %(n1, n2, n3)


# 通过对路由的判断，视图函数内部的执行可以进行业务逻辑的处理
@app.route('/show')
@app.route('/show/list')
@app.route('/show/<name>')
# 关键字传参
def show(name="ze"):
    re = request.path
    if re == '/show':
        return '我是show路由的结果'
    elif re =='/show/list':
        return '我是/show/list路由的结果'
    return "show %s" % name

# 模板
@app.route('/info')
def info():
    # 返回模板文件,可以传递变量
    # 语法:return render_template('xxx.html',变量1=值1,变量2=值2......)
    name = 'flask'
    age = 20
    return render_template("01-show.html", name=name, age=age)


if __name__ == "__main__":
    app.run(debug=True)
