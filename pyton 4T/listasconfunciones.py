lista=['pyton','lenguaje','programacion',9.03,'interpretado']

#añadiendo un elemento 
def adicionar():
    elemento=input("ingresar el valor a agregar")
    lista.append(elemento)
    mostrar()
    
#mostrando la lista 
def mostrar():
    for list in lista:
        print(list)
        
#modificando un valor 
def actualizar():
    updeelemento=input("ingrese el valor a agregar")
    lista[2]=updeelemento
    mostrar()
    
#borrando un valor
def Borrar():
    updelemento=input("ingrese el valor a agregar")
    lista.remove(updelemento)
    mostrar()
    
num=int(input("ingresa la opcion correspondiente 1 adiciona 2 para mostrar 3 actualizar")
match num
     case 1: adicionar()
     case 2: mostrar()
     case 3: actualizar()     
     case 4: Borrar()
     case _:print("opcion no valida")
     
     bucles listas vistas 