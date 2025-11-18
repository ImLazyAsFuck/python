a = int(input("Nhập điểm a: "))
b = int(input("Nhập điểm b: "))
c = int(input("Nhập điểm c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Ba cạnh không thể tạo thành tam giác")
else:
    print("Ba cạnh có thể tạo thành tam giác")