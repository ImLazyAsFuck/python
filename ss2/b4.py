number = int(input("Nhập số nguyên: "))
SUM = 0

for i in range(number + 1):
    SUM += i
print(f"Tổng các số từ 1 đến {number} là: {SUM}")