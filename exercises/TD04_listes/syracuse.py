def syracuse(n):
    suite = []
    while n != 1:
        if n % 2 == 0:
            n = n//2
            suite.append(n)
        else:
            n = n * 3 + 1
            suite.append(n)
    return suite


print(syracuse(3))


def testeConjecture(n_max):
    for i in range(1, n_max):
        if syracuse(i) == 1:
            pass

        else:
            return("False")
    return("True")
 

print(testeConjecture(10000))