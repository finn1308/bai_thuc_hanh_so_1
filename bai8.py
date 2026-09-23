TB = float(input(" Nhập điểm trung bình = "))
if TB >= 8:
    print(f"Điểm trung bình của bạn là {TB}, xếp loại Giỏi")
elif 7.9 >= TB >= 6.5:
    print(f"Điểm trung bình của bạn là {TB}, xếp loại Khá")
elif 6.4 >= TB >= 5:
    print(f"Điểm trung bình của bạn là {TB}, xếp loại Trung bình")
else:
    print(f"Điểm trung bình của bạn là {TB}, xếp loại Yếu")
