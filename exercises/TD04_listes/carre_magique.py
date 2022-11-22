carre_mag = [
 [4,  14,  15, 1],
 [9, 7, 6,  12],
 [5,  11,  10, 8],
 [ 16, 2, 3,  13]
]
for i in range(len(carre_mag)):
    for j in range(len(carre_mag[i])):
        print(carre_mag[i][j], end=" ")
    print()

carre_pas_mag = carre_mag
carre_pas_mag[3][2]= 7
print (carre_pas_mag)

print(len(carre_mag))