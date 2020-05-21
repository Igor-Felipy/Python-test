#map(função, *sequencia) --> Objeto map
def qua(x): return x**2

mapa = map(qua, [1,2,3,4,5]) # é necessario transformar um objeto map em tuplas ou listas
listmap = list(mapa)
ran = tuple(map(qua, range(10)))
lamb = list(map(lambda x: x**3, range(10)))

print('map(...) =',mapa)
print()
print('list(map(...)) = ',listmap)
print()
print('tuple(map(..., range()))=',ran)
print()
print('map(função lambda, ...)=')