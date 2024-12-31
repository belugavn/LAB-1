import pandas as pd
stocks1 = pd.read_csv('E:/stocks1.csv')

print("5 dòng đầu tiên của stocks1:")
print(stocks1.head())

print("\nKiểu dữ liệu của mỗi cột trong stocks1:")
print(stocks1.dtypes)

print("\nThông tin tổng quan của stocks1:")
print(stocks1.info())

stocks2 = pd.read_csv('E:/stocks2.csv')
print(stocks2)
stock = pd.concat([stocks1,stocks2])
print(stock)
avg = stock[['open','high','low','close']].values.mean()
print(avg.head())