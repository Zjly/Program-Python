from flask import Flask, request, render_template, redirect, Response
import json

# 默认配置
# 静态文件所在文件夹名字 static_folder:static
# 访问静态文件的前缀 static_url_path = ''
# 模板文件所在文件夹名字 template_folder:templates
app = Flask(__name__)


# 使用route装饰器配置路由
@app.route("/")
def hello():
	return "hello world!"

@app.route("/hello")
def he():
	return "你好"

# ip + port + /路径 + 变量
@app.route("/user/<username>")
def user(username):
	return username


@app.route("/login/<int:id>")
def login(id):
	return "id", id

# GET
# 请求方式 url+?a=a&b=b&c=c
@app.route("/list", methods={"GET"})
def list():
	print(request.method)
	print(request.args)
	print(request.args.get("id"))
	print(request.args.get("num"))
	return "hello"

# POST
@app.route("/search", methods={"POST"})
def search():
	print(request.method)
	print(request.form)
	print(request.form.get("id"))
	print(request.form.get("num"))
	return "hello"

# 文件处理
@app.route("/classify", methods={"POST"})
def classify():
	print(request.files.get("file"))
	f = request.files.get("file")
	f.save("./a.jpg")
	return "hello"

# 接口文档 url + 请求方式 + 参数

# 渲染
# 文件处理
@app.route("/admin")
def admin():
	# jinjia2模板引擎
	# render_template(模板，动态数据)
	user = request.args.get("username")
	return render_template("admin.html", result=user)

# 重定向
@app.route("/re")
def re():
	return redirect("/admin")

# 返回json
@app.route("/jsonstr", methods={"GET"})
def jsonstr():
	return Response(json.dumps({"code":0, "name":"小明", "pwd":123}), content_type="application/json")

# 入口
if __name__ == '__main__':
	# ip port 调试模式（热更新）
	# 127.0.0.1 localhost 0.0.0.0
	app.run(host="127.0.0.1", port="5000", debug=True)
