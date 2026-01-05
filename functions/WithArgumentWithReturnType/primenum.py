def check_prime(num):
    if num <= 1:
        return "Not Prime"

    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    return "Prime"

n = int(input("Enter a number: "))
result = check_prime(n)
print("The number is", result)
