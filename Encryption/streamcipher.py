import random

#64-bit binary 
def genBinary(seed):
    #seed the random generation guarentee replication of generation of plaintext and/or key
    random.seed(seed)
    b = random.getrandbits(64)
    #binary = format(b, "b")
    return(b)

#encrypt
def cipherText(plain_text, key):
    cipher_txt = plain_text ^ key
    #cipher_txt = str(cipher_txt)
    return(cipher_txt)

#decrypt
def plainText(cipher_txt, key):
    plain_txt = cipher_txt ^ key
    #plain_txt = str(plain_txt)
    return(plain_txt)

#Main

if __name__ == "__main__":
    print("Welcome to Mike's magical Stream Cipher!\n")
    plain_text = genBinary(int(raw_input("Please enter a number to be the seed for the plaintext generation :")))
    print("plaintext is : " + str(plain_text))
    key = genBinary(int(raw_input("Please enter a number to be the key for the plaintext generation :")))
    print("key is : " + str(key))
    c = cipherText(plain_text, key)
    print("The encrypted text is : " + str(c))
    print("The decrypted text is : " + str(plainText(c, key)))
