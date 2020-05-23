from random import randrange

my_name = "Jason Wang"
userid = "jjw6188"
# also name your file userid.py

def gcd(a, b):
    # Your code here
    #Base case (Remainder is 0)
    if a == 0: 
        return b
    #Recursively call gcd function
    else:
        remain = b%a
        return gcd(remain,a)

def inverse(a, b):   # use extended euclidean algorithm to find inverse
    # Your code here    
    #Base case
    gcd,s,t = backwardpass(a,b)
    return s

def backwardpass(a, b):
    if a == 0:
        #In the format gcd,s,t
        gcd = b
        return gcd,0,1
    else:
        gcd,s,t = backwardpass(b%a,a)

        quo = b//a
        return gcd,t-(quo)*s,s

def generate_key(a, b):
    # Your code here
    n = a*b
    k = (a-1)*(b-1)
    #Excludes 1, but includes k as a possiblity for e
    e = randrange(2,k)
    #Loop runs until a random e is found that is co-prime with k 
    while gcd(e,k) !=1:
        e = randrange(2,k)
    d = inverse(e,k)
    if d < 0:
        d = k + d
    keys = ((e,n),(d,n))
    return keys
    # (e, n) is public, (d, n) is private
    # return ((e, n), (d, n))


def encrypt(public_key, txt):
    # Your code here
    encrpytion = []
    for ele in txt:
        m = ord(ele)
        c = (m**public_key[0])%public_key[1]
        #Append this cipher into encrpytion
        encrpytion.append(c)
    return encrpytion

def decrypt(private_key, ciphers):
    # Your code here
    decrpytion = []
    for i in range(len(ciphers)):
        m = (ciphers[i]**private_key[0])%private_key[1]
        #Append m in the form of a character into decryption
        decrpytion.append(chr(m))
    return "".join(decrpytion)


print(ord(y))