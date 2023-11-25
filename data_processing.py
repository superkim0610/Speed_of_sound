import csv
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

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
print(y_train)

model = LinearRegression()
model.fit(x_train, y_train)

print("가중치(계수, 기울기 파라미터 W) :", model.coef_)
print("편향(절편 파라미터 b) :", model.intercept_)

print(model.score(x_train, y_train))
print(model.score(x_test, y_test))

plt.scatter(x, y, color='black')

def remove_outliers(x, y, model, threshold):
    y_pred = model.predict(x)
    residuals = np.abs(y - y_pred)
    x_filtered = x[residuals < threshold]
    y_filtered = y[residuals < threshold]
    return x_filtered, y_filtered

data = pd.read_csv('data_csv.csv')
x, y = data.iloc[:, 0], data.iloc[:, 1]
x = x.to_frame()

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

outlier_threshold = 10

x_train_filtered, y_train_filtered = remove_outliers(x_train, y_train, model, outlier_threshold)
x_filtered, y_filtered = remove_outliers(x, y, model, outlier_threshold)

model.fit(x_train_filtered, y_train_filtered)

plt.scatter(x_filtered, y_filtered, color='b')
plt.plot(x, model.predict(x), color='r')

plt.xlim(24,29)
plt.ylim(0, 400)

plt.plot([24, 29], [345.4, 348.4], color='g')

plt.legend()
plt.show()

