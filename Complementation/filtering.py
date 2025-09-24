from numpy import nan as NA
import pandas as pd

data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 5.]])
print(data)
print("-"*10)
#Fill những cái bị NA bằng các chỉ số trung bình của cột
cleaned=data.fillna(data.mean())
print(cleaned)