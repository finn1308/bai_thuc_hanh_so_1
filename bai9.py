elec = int(input("Nhập số kWh tiêu thụ:"))
if elec <= 50:
    e1 = elec * 1800
    print(f"Số tiền điện phải trả là: {e1} VND")
elif elec  <= 100:
    e2 =  50*1800+(elec-50)*2000
    print(f"Số tiền điện phải trả là: {e2} VND")
else :
    e3 =  50*1800+50*2000+(elec-100)*2500
    print(f"Số tiền điện phải trả là: {e3} VND")
