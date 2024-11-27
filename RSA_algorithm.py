"""
Author: James Rota

RSA --> Encryption, Practice and Deep learning of how it works.

Test Users: John, Bob, Jan.

Given by messages sent between them --> test1, test2, test3

Steps: 

1. Key Generation

--> Choose random prime numbers p and q (should be large and a large diff between them)
    --> Where n = pq


2. Key Distribution

3. Encryption

4. Decryption

"""

import random

"""
Logic - RSA algorithm 

"""

# Reference https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

class RSA_User():
    def __init__(self, name):
        self.name = name
        self.public_key, self.private_key = self.key_generation()

    def primeGeneration(self):
        minPrime = 0
        maxPrime = 1000
        cached_primes = [i for i in range(minPrime,maxPrime) if is_prime(i) == True]
        prime = random.choice(cached_primes)

        return prime

    def key_generation(self):

        p = self.primeGeneration()
        q = self.primeGeneration()

        while q == p:
            q = self.primeGeneration()

        n = p * q

        e = 65537 # General RSA value for e
        totient_n = (p - 1) * (q - 1)

        d = pow(e, -1, totient_n)

        return (e, n), (d, n)

    def encrypt(self, plaintext, public_key):
        e, n = public_key
        return [pow(ord(char), e, n) for char in plaintext]
    
    def decrypt(self, ciphertext):
        d, n = self.private_key
        return ''.join([chr(pow(char, d, n)) for char in ciphertext])


f = open("Test_Documents/test1.txt", "r")
message = f.read()
f.close()

Bob = RSA_User("Bob")
Jan = RSA_User("Jan")

Bob.key_generation()
Jan.key_generation()

encrypted_message = Bob.encrypt(message, Jan.public_key)

decrypted_message = Jan.decrypt(encrypted_message)

print(f'This is the encrypted message: {encrypted_message},\n' +
      f'This is the decrypted message: {decrypted_message}')
    



