import pandas as pd

stocks1 = pd.read_csv('E:/stocks1.csv')

# Hiển thị 5 dòng đầu tiên của stocks1
print("5 dòng đầu tiên của stocks1:")
print(stocks1.head())

# Hiển thị kiểu dữ liệu của mỗi cột trong stocks1
print("\nKiểu dữ liệu của mỗi cột trong stocks1:")
print(stocks1.dtypes)

# Xem thông tin tổng quan của stocks1
print("\nThông tin tổng quan của stocks1:")
print(stocks1.info())

import pandas as pd

# Đọc file stocks1.csv vào DataFrame stocks1
stocks1 = pd.read_csv('stocks1.csv')

# Kiểm tra xem trong stocks1 có dữ liệu Null nào không
print("Kiểm tra dữ liệu Null:")
print(stocks1.isnull().sum())

# Thay thế dữ liệu Null ở cột high bằng giá trị trung bình của cột high
mean_high = stocks1['high'].mean()
stocks1['high'].fillna(mean_high, inplace=True)

# Thay thế dữ liệu Null ở cột low bằng giá trị trung bình của cột low
mean_low = stocks1['low'].mean()
stocks1['low'].fillna(mean_low, inplace=True)

# Hiển thị thông tin tổng quan để xác nhận không còn dữ liệu Null
print("\nThông tin tổng quan của stocks1 sau khi xử lý dữ liệu Null:")
print(stocks1.info())
