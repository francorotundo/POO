import random

def ordenamiento_por_mezcla(lista):
    if len(lista)>1:
        medio = len(lista) //2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        #Llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        #Iteradorespara recorrer las dos sublistas
        i = 0
        j = 0

        #Iterador para lista principal
        k = 0

        while i<len(izquierda) and j<len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i+=1
            else:
                lista[k] = derecha[j]
                j+=1

            k+=1
        
        while i<len(izquierda):
            lista[k] = izquierda[i]
            i+=1
            k+=1

        while j<len(derecha):
            lista[k] = derecha[j]
            j+=1
            k+=1

    return lista

if __name__ == '__main__':
    tamaño_de_lista = int(input('De que tamaño sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]
    print(lista) 
    print('-'*20)   
    
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)
