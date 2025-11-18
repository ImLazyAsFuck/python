number = int(input("Nhập số nguyên: "))
factorial = 1

for i in reversed(range(2, number + 1)):
    factorial *= i
print(f"Giai thừa của {number} là: {factorial}")