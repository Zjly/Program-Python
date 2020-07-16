from flask import Flask, Response, json
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

# 连接数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/test"

db = SQLAlchemy(app)


# 构建数据模型
class Garbage(db.Model):
	__tablename__ = "test"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), unique=True)
	type = db.Column(db.Integer, unique=True)

	def __init__(self, name, type):
		self.name = name
		self.type = type

	# 重写
	def __repr__(self):
		return self.name


# 数据操作
class GarbageInfo():
	def __init__(self):
		self.__fields__ = ["id", "name", "type"]

	def findAll(self):
		# *
		return Garbage.query.all()

	def findByType(self, find_type):
		# 根据条件筛选query.filter_by()	query.filter()	query.slice(i,i+10)
		return Garbage.query.filter_by(type=find_type).all()


# 要处理的数据格式 一个garbage对象，数组[garbage对象，]
# 遍历 根据需要的属性 构造新的对象
# 数据处理方法 把任何继承db.model的数据模型对象处理成json可以解析的
def class_to_data(data_list, fields, type=0):
	# 数组
	if not type:
		list = []
		for item in data_list:
			temp = {}
			for f in fields:
				# id name type		username pwd time 单独判断需要特殊处理的字段
				if f in ["c_time", "u_time", "d_time"]:
					temp[f] = datetime.datetime.strftime(getattr(item, f), "%Y-%M-%D %H:%M:%S")
				temp[f] = getattr(item, f)
			list.append(temp)
	else:
		list = {}
		for f in fields:
			list[f] = getattr(data_list, f)

	return list


# 配合路由使用
@app.route("/")
def all():
	garbageInfo = GarbageInfo()
	data = garbageInfo.findAll()
	result = class_to_data(data, garbageInfo.__fields__, 0)

	return Response(json.dumps({"status": 200, "data": result}))


if __name__ == '__main__':
	# garbageInfo = GarbageInfo()
	# data = garbageInfo.findAll()
	# data = garbageInfo.findByType(11)
	# print(data)

	app.run(debug=True)
