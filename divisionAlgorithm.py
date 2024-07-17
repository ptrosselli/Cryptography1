#Thomas Rosselli
#Utsav
#Robert Long
#Shaoib

import math

#array copy
def copy(arr1, arr2):
    for i in range(len(arr1)):
        arr2[i] = arr1[i]
    return arr2

#request first and second
x = int(input("Enter x: "))
y = int(input("Enter y: "))

#show formatting
print("[u1, v1, u2, v2, u3, v3, q]")

#calculate gcd
gcd = math.gcd(x, y)

#Make arrays
arr = [1, 0, 0, 1, x, y, 0]
old = copy(arr, arr)
new = [-1, -1, -1, -1, -1, -1, -1]

#perform algorithm while we have to
while old[4] != gcd:
    print("----")
    print(old)
    new[6] = old[4] // old[5]
    new[0] = old[1]
    new[2] = old[3]
    new[4] = old[5]
    new[1] = old[0] - (old[1] * new[6])
    new[3] = old[2] - (old[3] * new[6])
    new[5] = old[4] - (old[5] * new[6])
    old = copy(new, old)

print("x: " + str(old[0]) + ", y: " + str(old[2]) + ", gcd: " + str(old[4]))
