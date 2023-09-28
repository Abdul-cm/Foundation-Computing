# isprime function
def isprime(n):
    for i in range (2,n-1):
        if (n%i==0):
            return False
        else:
            return True

answer = isprime(7)
print(answer)
