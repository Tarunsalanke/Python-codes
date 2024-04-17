def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
# Main program
user_input = int(input("Enter a number: "))
if is_prime(user_input):
    print("Prime number")
else:
    print("Not a Prime number")