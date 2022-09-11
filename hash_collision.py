import hashlib
import random
import string

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    x = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    sha = hashlib.sha256(string.encode())
    sha = int(sha.hexdigest(), base=16)
    xBitString = format(sha, 'b')
    hashes = { x: xBitString }
    y = b'\x00'

    while True:
        y = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

        sha = hashlib.sha256(string.encode())
        sha = int(sha.hexdigest(), base=16)
        yBitString = format(sha, 'b')
        yBitStringLength = len(yBitString)
        yBits = yBitString[yBitStringLength - k:]

        for str, bitStr in hashes.items():
            bitStringLength = len(bitStr)
            bits = bitStr[bitStringLength - k:]
            if bits == yBits:
                return str.encode('utf-8'), y.encode('utf-8')

        hashes[y] = yBitString