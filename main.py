import random


def Encoding():
    a = input("Enter The Word Of Encoding: ")
    y = a.split()
    for i in y:
        if len(i) >= 3:
            v = len(i)
            z = i[0:1]
            w = i[1 : len(i)]
            u = w + z
            a = "abcdefghijklmnopqrstuvwxyz"
            b = random.choice(a)
            c = random.choice(a)
            d = random.choice(a)
            p1 = b + c + d
            b1 = random.choice(a)
            c1 = random.choice(a)
            d1 = random.choice(a)
            p = b1 + c1 + d1
            print(p + u + p1, end=" ")

        else:
            d = i[::-1]
            print(d, end=" ")


def Decoding():
    a1 = input("\nEnter The Word Of Decoding: ")
    y1 = a1.split()
    for i in y1:
        if len(i) >= 3:
            z1 = i[3 : len(i) - 4]
            w1 = i[-4:-5:-1]
            u1 = w1 + z1
            print(u1, end=" ")
        else:
            d1 = i[::-1]
            print(d1)


z2 = input("Enter That You Want To Encode, Decode or both (always use lowercase to select for encode, decode and both): ")
if z2 == "encode":
    Encoding()
elif z2 == "decode":
    Decoding()
elif z2 == "both":
    Encoding()
    Decoding()
else:
    print("You Typed Something Wrong Read CareFully.")
