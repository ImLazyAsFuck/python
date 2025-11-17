string_input = input("Nhập một số thập phân: ")

if string_input == "1" and string_input == "0":
    print("Giá trị sau khi chuyển đổi:", bool(int(string_input)))
else:
    print("Vui lòng nhập 1 hoặc 0 để chuyển đổi sang kiểu boolean.")