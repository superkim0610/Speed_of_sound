import csv
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

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

data = pd.read_csv('data_csv.csv')
x, y = data.iloc[:, 0], data.iloc[:, 1]
x = x.to_frame()

print(x.head());print(y.head())

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)
print(x_train)

model = LinearRegression()
model.fit(x_train, y_train)

print("가중치(계수, 기울기 파라미터 W) :", model.coef_)
print("편향(절편 파라미터 b) :", model.intercept_)

print("훈련세트 점수: {:.2f}".format( model.score(x_train, y_train) ))
print("테스트세트 점수: {:.2f}".format( model.score(x_test, y_test) ))