def generaPares(limite):
    num=1
    lista=[]
    while num<limite:
        lista.append(num*2)
        num+=1
    return lista

print(generaPares(10))

def iterablePares(limite):  # Hace lo mismo que la función generaPares, pero es más eficiente
    num=1
    while num<limite:
        yield num*2  # Devuelve un objeto iterable
        num+=1

print(generaPares(10))

x=iterablePares(10)
for i in iterablePares(10):
    print(i)

print("\n",next(x))
# Stand by del generador...
print("\n",next(x))
# Stand by del generador...