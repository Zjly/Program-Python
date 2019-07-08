import pandas as pd
import pymysql

conn = pymysql.connect("localhost", "root", "root", "test")
courses = pd.read_sql(sql="select course_name, course_type from cm_course", con=conn)
courses.columns = ["name", "type"]

courses = courses.replace(" ", "", regex=True)
courses = courses.replace("\n", "", regex=True)
courses = courses.replace("\\?", "", regex=True)
courses = courses.replace("交流与写作类", "人文与社会类", regex=True)
courses = courses.replace("中国与全球类", "中华文化与世界文明", regex=True)
courses = courses.replace("研究与领导类", "人文与社会类", regex=True)
courses = courses.replace("艺术体验与审美鉴赏", "艺术与欣赏类", regex=True)
courses = courses.replace("社会科学与现代社会", "人文与社会类", regex=True)
courses = courses.replace("科学精神与生命关怀", "自然与工程类", regex=True)
courses = courses.replace("数学与推理类", "自然与工程类", regex=True)
courses = courses.replace("中华文化与世界文明", "人文与社会类", regex=True)

courses.to_csv("courses.csv", sep=",", index=None)
