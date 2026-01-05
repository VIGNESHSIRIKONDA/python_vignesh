def check_prime():
    num = int(input("Enter a number: "))

    if num <= 1:
        print("Not Prime")
        return

    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            return
    print("Prime")

check_prime()
