N = int(input(" Nhập một số từ 1 đến 9 : "))
if 1 <= N <= 9:
    print (" Bảng cửu chương là : ")
    for bcc in range(1, 11):
        print (f"{N} x {bcc} = {N*bcc}")
else:
    print (f" số {N} không hợp lệ")
