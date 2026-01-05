def check_prime():
    num = int(input("Enter a number: "))

    if num <= 1:
        return "Not Prime"

    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    return "Prime"

result = check_prime()
print("The number is", result)
