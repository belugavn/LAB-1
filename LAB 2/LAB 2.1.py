import numpy as np
nhietdo = np.random.uniform(5,30,30)
nhietdo1= np.round(nhietdo , decimals = 2)
print(nhietdo1)

nhietdo_tb1 = np.mean(nhietdo1)
nhietdo_tb1 = np.mean(nhietdo1)
print("Nhiệt độ trung bình trong tháng là",nhietdo_tb1)

nhietdo_thap = min(nhietdo1)
nhietdo_cao = max(nhietdo1)
print(nhietdo_thap,nhietdo_cao)

nhietdo_chenhlech = np.diff(nhietdo1)
print(nhietdo_chenhlech)

nhietdo_chenhlechcaonhat = max(nhietdo_chenhlech)
ngay_chenhlechcaonhat = np.argmax(np.abs(nhietdo_chenhlech))+1
print(f"Ngày có nhiệt độ chênh lệch cao nhất là:" , ngay_chenhlechcaonhat)

nhietdolonhon20 = np.where(nhietdo1 > 20)[0] + 1
print(f"Ngày có nhiệt độ lớn hơn 20 ",nhietdolonhon20)
# Tất cả các ngày có nhiệt độ cao hơn 20 độ C
days_above_20 = np.where(temperatures > 20)[0] + 1
temps_above_20 = temperatures[temperatures > 20]

print("\nCác ngày có nhiệt độ cao hơn 20 độ C:", days_above_20)
print("Nhiệt độ các ngày đó:", temps_above_20)

# Lấy nhiệt độ của ngày 5, 10, 15, 20, và 25
selected_days = [5, 10, 15, 20, 25]
selected_temps = temperatures[np.array(selected_days) - 1]

print("\nNhiệt độ của ngày 5, 10, 15, 20, và 25:", selected_temps)

# Nhiệt độ của các ngày có nhiệt độ trên trung bình
days_above_avg = np.where(temperatures > average_temp)[0] + 1
temps_above_avg = temperatures[temperatures > average_temp]

print("\nCác ngày có nhiệt độ trên trung bình:", days_above_avg)
print("Nhiệt độ các ngày đó:", temps_above_avg)

even_days_temps = temperatures[np.arange(1, 31, 2) - 1]
odd_days_temps = temperatures[np.arange(0, 30, 2)]

print("\nNhiệt độ của các ngày chẵn trong tháng:", even_days_temps)
print("Nhiệt độ của các ngày lẻ trong tháng:", odd_days_temps)
