num = int(input("Enter a number: "))

factor_count = 0

for i in range(1, num + 1):
    if num % i == 0:  # checks if i is a factor
        factor_count += 1

print("Number of factors of", num, "is:", factor_count)
