import random

def genKey(p, g, a):
    key = g^a % p #mind the gap
    return(key)


if __name__ == "__main__":
    P = random.getrandbits(16)
    G = random.getrandbits(16)
    #alice "Chooses" a and gets her public key and sends it to bob
    a = random.getrandbits(16)
    alice_key = genKey(P, G, a)
    print("This is my key - Alice : " + str(alice_key))
    #Bob "Chooses" b and gets his public key and sends it to alice
    b = random.getrandbits(16)
    bob_key = genKey(P, G, b)
    print("This is my key - Bob : " + str(bob_key))

    #generate secret keys

    alice_Skey = bob_key^a % P
    bob_Skey = alice_key^b % P

    print("Alice's secret key: " + str(alice_Skey))
    print("Bob's secret key: " + str(bob_Skey))