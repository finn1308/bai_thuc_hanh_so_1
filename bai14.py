import random
Z = random.randint(1, 10)
num = int(input("Ngẫu nhiên một số từ 1 đến 10 :"))
if num < Z :
        print(f"Bạn nhập số {num} nhỏ hơn {Z}")
elif num > Z :
        print(f"Bạn nhập số {num} lớn hơn {Z}")
elif num < 1 or num > 10:
        print(f" Số bạn nhập là {num} không hợp lệ ")
else: 
        print(f"Bạn nhập số {num} bằng {Z}")
