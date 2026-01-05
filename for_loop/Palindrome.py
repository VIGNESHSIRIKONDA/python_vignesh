num = 121
rev = 0
temp = num

for i in range(len(str(num))):
    rev = rev * 10 + temp % 10
    temp //= 10

if rev == num:
    print("Palindrome")
else:
    print("Not Palindrome")
