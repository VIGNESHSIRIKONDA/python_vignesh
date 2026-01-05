num = int(input("Enter a number: "))
factor_count = 0
i = 1

while i <= num:
    if num % i == 0:
        factor_count += 1
    i += 1

print("Number of factors of", num, "is:", factor_count)
