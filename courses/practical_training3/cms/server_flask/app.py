from flask import Flask, request
import json
from flask_cors import CORS

app = Flask(__name__)

# 跨域 flask-cors
CORS(app, supports_credential=True)

# 折线图 平均工资 无参数 get
@app.route("/line")
def line():
	with open("./json/average.json", "r") as f:
		content = json.load(f)
		return json.dumps({"status": 200, "data": content})


# 饼图 百分比 无参数 get
@app.route("/pie")
def pie():
	with open("./json/pie.json", "r") as f:
		content = json.load(f)
		return json.dumps({"status": 200, "data": content})


# 词云图 参数: num get
@app.route("/cloud")
def cloud():
	num = request.args.get("num")
	with open("./json/count_list.json", "r") as f:
		content = json.load(f)
		# content中取num条
		result = []
		for i in range(int(num)):
			result.append(content[i])
		return json.dumps({"status": 200, "data": result})


app.run(debug=True)
