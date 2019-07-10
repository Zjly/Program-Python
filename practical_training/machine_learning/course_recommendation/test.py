import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(3, 5),
				  index=["地区1", "地区2", "地区3"],
				  columns=["北京", "天津", "上海", "广州", "沈阳"])
print(df.loc["地区1", "北京"])
