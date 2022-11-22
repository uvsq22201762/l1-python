
def syracuse(n):  
    if n == 1:
        return [1]
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
        l = syracuse(i)
        if l[-1] == 1:
            pass
        else : 
            return False
    return True
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    pass
ghgh

print(testeConjecture(10000))

def tempsVol(n):
    l_1 = syracuse(n)
    if l_1[0] == 1:
        return ("0")
    else:    
        return len(syracuse(n))
    """ Retourne le temps de vol de n """
    pass

print("Le temps de vol de", 3, "est", tempsVol(3))


def tempsVolListe(n_max):
    return[tempsVol(i) for i in range(1, n_max)]
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    pass

print(tempsVolListe(100))




