
def ordenarLista(lista):
    if len(lista) <= 1 : # Si la extension de la lista es menos o igual a 1 retorna la lista
        return lista
    
    pivote = lista[len(lista) // 2] # Crea un pivote a la mitad de la lista
    
    #Se crean las sub listas
    izq = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    der = [x for x in lista if x > pivote]
    
    return ordenarLista(izq) + ordenarLista(centro) + ordenarLista(der)

lista = [7,34,1,23,40,78,8,123]
print(lista)
print(ordenarLista(lista))