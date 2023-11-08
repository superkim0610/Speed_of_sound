import csv
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def txt_to_csv():
    data_dict = {'temp': [], 'speed':[]}

    with open('2023-09-13_15-49-20_455190.txt', 'r') as f:
        for l in f:
            _d = eval(l)
            data_dict['temp'].append(_d['temp'])
            data_dict['speed'].append(_d['speed'])

    data_df = pd.DataFrame(data_dict)
    data_df.to_csv('data_csv.csv', index=False)

 
# by pandas ---------

# data = pd.read_csv('data_csv.csv')
# x, y = data['temp'], data['speed']

# print(x.head())

# x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)
# # x_train = list(map(lambda x: x[1], x_train))
# x.reshape(-1, 1)
# print(x_train)

# by np

x = np.zeros()
y = np.array()

with open('data_csv.csv', 'r') as f:
    _f = csv.reader(f)
    for l in _f:
        x.append(l[0])
        y.append(l[1])

print(x);print(y)

# model = LinearRegression()
# model.fit(x_train, y_train)

# print("가중치(계수, 기울기 파라미터 W) :", model.coef_)
# print("편향(절편 파라미터 b) :", model.intercept_)

# print("훈련세트 점수: {:.2f}".format( model.score(x_train, y_train) ))
# print("테스트세트 점수: {:.2f}".format( model.score(x_test, y_test) ))