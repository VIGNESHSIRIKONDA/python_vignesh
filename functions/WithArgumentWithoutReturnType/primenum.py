def check_prime(num):
    if num <= 1:
        print("Not Prime")
        return

    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            return
    print("Prime")

n = int(input("Enter a number: "))
check_prime(n)
