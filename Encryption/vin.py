# Vincere Encryption

#accepts key and generates a key function

def genKey(str, key):
    key = list(key)
    #if the length of the key must not be the length of the plaintext for added security
    if len(str) == len(key):
        return(key)
    #if the key is not length of plaintext then repeat the key in a circular manner to match the...
    #...length of the plaintext
    else:
        for i in range(len(str) - len(key)):
            key.append(key[i % len(key)])
    #re-combine the key into a single string
    return("".join(key))


#encrypt the paintext/decrpyt the cypher text function given the key

#to encrypt the plaintext str and key are added modulo 26
# Ei = (Pi + Ki) % 26 + 0 (offset)
def cipherTxt(str, key):
    #create empty array to store the ciphertext as we encrypt
    cipher_txt = []
    for i in range(len(str)):
        #use ord() to convert char's into integers for the maths
        crypt = (ord(str[i]) + ord(key[i])) % 26
        #not sure if we need to include the offset so in this case ill just do offset = 0 ...
        #... which is ord('A')
        crypt += ord('A')
        #re-convert the integers into characters then append them into a cipher_txt array
        cipher_txt.append(chr(crypt))
    return("".join(cipher_txt))

#Decryption based on cipher_txt and key
# Di = (Ei - Ki + 26) % 26 + 0 (Offset)
def plainTxt(cipher_txt, key):
    #create empty array to hold decrpyted plaintext
    plain_txt = []
    #from 0 to len(ciphertext) 
    for i in range(len(cipher_txt)):
        decrypt = (ord(cipher_txt[i]) - ord(key[i]) + 26) % 26
        decrypt += ord('A')
        plain_txt.append(chr(decrypt))
    return("".join(plain_txt))



#Main
if __name__ == "__main__":
    print("WELCOME TO MICHAELS VINGENERE CIPHER\n")
    #Ability to select encrypt or decrypt
    print("If you would like to encrypt a message? Enter A\n")
    print("Decrypt? Enter B\n")
    c = raw_input("Enter A () or B here ---> ")
    sel = c.upper()
    # print(sel)
    if sel == 'A':
        plainStr = raw_input("What string would you like to encrypt :").upper()
        plainStr = "".join(plainStr.split())
        print("This is the plain string: " + plainStr)
        keyword = raw_input("What is the key that you wish to use :").upper()
        key = genKey(plainStr, keyword)
        print("Key is (keep this for decrpytion):" + key)
        print("The Cipher Text is: " + cipherTxt(plainStr, key))
    else:
        cipherStr = raw_input("What is the encrypted message you'd like to decipher :").upper()
        key = raw_input("What is the key to decrypt the message (NOTE: not the KEYWORD the KEY generated when encrypting):").upper()
        print("The decrypted message is: " + plainTxt(cipherStr, key))

