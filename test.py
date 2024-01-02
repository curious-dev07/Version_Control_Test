## check for prime Number or not.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
        
    return True
number = int(input("Enter Number : "))

if is_prime(number):
    print(f"{number} ===> PRIME")
else: 
    print(f"{number} ===> NOT  PRIME") 