alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cipher = input("Enter ciphertext: ")

c = list(cipher)

for index in range(1,26):
    cc = c
    for x in range(len(cc)):
        if cc[x] == ' ':
            continue
        cc[x] = alph[(alph.index(cc[x]) + index) % 26]
    j = " "
    print(index, ": ", j.join(cc))






