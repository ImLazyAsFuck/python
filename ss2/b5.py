number = input("Nhập số nguyên: ")
left = 0
right = len(number) - 1
is_palindrome = True

for i in range(len(number) // 2):
    if number[left] != number[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
print(f"Số vừa nhập {'là' if is_palindrome else 'không phải là'} số đối xứng")