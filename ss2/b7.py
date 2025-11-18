a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
prime_numbers = []

if a >= b or a <= 0:
    print("Số a phải nhỏ hơn số b và a b phải lớn hơn 0")
else:
    for i in range(a, b + 1):
        if i < 2:
            continue
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    print(f"Các số nguyên tố trong khoảng từ {a} đến {b} là: {prime_numbers}")