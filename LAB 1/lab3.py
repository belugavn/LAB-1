import pandas as pd

# Đọc file stocks1.csv vào DataFrame stocks1
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

