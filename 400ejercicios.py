#hemos cambiado para saber si funciona
#ejercicio 277
#lista = int(input('escriba lista: '))

lista = [1,3,6,10]
newlist = []
for elemento in range(1,len(lista)):
    i=lista[elemento] - lista[elemento-1]
    print(i)
    newlist.append(i)

print(sum(newlist))
