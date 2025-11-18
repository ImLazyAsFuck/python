n = int(input("Nhap mot so nguyen: "))

if n % 3 == 0 and n % 5 == 0:
    print("Số vừa nhập chia hết cho cả 3 và 5")
elif n % 3 == 0:
    print("Số vừa nhập chia hết cho 3")
elif n % 5 == 0:
    print("Số vừa nhập chia hết cho 5")
else:
    print("Số vừa nhập không chia hết cho 3 hoac 5")
