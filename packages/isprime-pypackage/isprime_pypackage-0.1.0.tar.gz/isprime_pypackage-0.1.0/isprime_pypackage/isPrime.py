def isPrime(number):
    check = False
    if number <= 1:
        return False
    else:
        for i in range (2, number):
            if number % i == 0:
                check = True
                break
        
    if check == True:
        return False # return False if number is not prime
    else:
        return True # return True if number is prime