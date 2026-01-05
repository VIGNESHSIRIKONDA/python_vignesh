num = 28
i = 1
total = 0

while i < num:
    if num % i == 0:
        total += i
    i += 1

if total == num:
    print("Perfect number")
else:
    print("Not perfect number")
