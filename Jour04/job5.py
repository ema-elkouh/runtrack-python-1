L= [i for i in range(6)]
print(L[1])

def remplace():
    L.insert(3, L[2]+L[4])
    L.remove(L[4])
    return(L[3])

print(remplace())
print(L[5])