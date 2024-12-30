import numpy as np
# Đọc dữ liệu từ tập tin efficiency.txt vào danh sách efficiency
with open('E:/efficiency.txt', 'r') as file:
    efficiency = [int(line.strip()) for line in file]

# Đọc dữ liệu từ tập tin shifts.txt vào danh sách shifts
with open('E:/shifts.txt', 'r') as file:
    shifts = [line.strip() for line in file]

# In kết quả để kiểm tra
print('Efficiency:', efficiency)
print('Shifts:', shifts)

# Đọc dữ liệu từ tập tin efficiency.txt vào danh sách efficiency
with open('efficiency.txt', 'r') as file:
    efficiency = [int(line.strip()) for line in file]

# Đọc dữ liệu từ tập tin shifts.txt vào danh sách shifts
with open('E:/shifts.txt', 'r') as file:
    shifts = [line.strip() for line in file]

# Chuyển đổi danh sách thành mảng NumPy
np_efficiency = np.array(efficiency)
np_shifts = np.array(shifts)

# Kiểm tra kích thước của các mảng
print("Kích thước của np_efficiency:", np_efficiency.shape)
print("Kích thước của np_shifts:", np_shifts.shape)

# Lọc các giá trị hiệu suất của nhân viên làm việc vào ca 'Morning'
if np_efficiency.shape[0] == np_shifts.shape[0]:
    morning_efficiency = np_efficiency[np_shifts == 'Morning']

    # Tính hiệu suất sản xuất trung bình
    average_morning_efficiency = np.mean(morning_efficiency)

    print("Hiệu suất sản xuất trung bình của những nhân viên làm việc vào ca 'Morning':", average_morning_efficiency)
else:
    print("Số lượng phần tử trong np_efficiency và np_shifts không khớp.")

# Tạo mảng NumPy từ danh sách
np_efficiency = np.array(efficiency)
np_shifts = np.array(shifts)

# Lọc các giá trị hiệu suất của nhân viên làm việc trong các ca khác (không phải 'Morning')
non_morning_efficiency = np_efficiency[np_shifts != 'Morning']

# Tính hiệu suất sản xuất trung bình
average_non_morning_efficiency = np.mean(non_morning_efficiency)

print("Hiệu suất sản xuất trung bình của những nhân viên làm việc trong các ca khác (không phải 'Morning'):", average_non_morning_efficiency)

# Định nghĩa dtype cho mảng structured array
worker_dtype = np.dtype([('shift', 'U10'), ('efficiency', 'float')])

# Tạo mảng structured array workers
workers = np.array(list(zip(shifts, efficiency)), dtype=worker_dtype)

# In kết quả và kiểm tra kiểu dữ liệu
print(workers)
print("Kiểu dữ liệu của workers:", workers.dtype)
