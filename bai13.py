n = int(input(" Nhập n số nguyên: "))
for N in range(1,n+1):
    if N % 2 == 0:
        print(f"Số thứ {N} là số chẵn.")
    else:
        print(f"Số thứ {N} là số lẻ.")
