listaalias=["1k papa","2k cebolla","pan","criollos"]
print(listaalias)#mostramos la variable con el print la lista 
print(listaalias[0])#buscamos que valor queremos en la lista de los n° enteros
listaalias.append("mermelada")#agregar elementos en la lista con append()
print(listaalias)
listaalias.insert(0,"sal")#inserta una bariable en la posicion que se le indique en la lista 
print(listaalias)
listaalias.pop()#borramos el ultimo elemento de la lista
print(listaalias)
# busqueda de elementos por nombre en la lista, si esta o no en la lista 
be=input("busca un elemnto de la lista si/no: ")#el input guardamos un valor dentro de una bariable
if be=="si":
    elemento=input("ingrese el elemento que desea buscar:")
    if elemento in listaalias:
        print("el elemento se encuentra")
    else:#sino esta en la lista utilizamos el else
        print("el elemento no esta en la lista")