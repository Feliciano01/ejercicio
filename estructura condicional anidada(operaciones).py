print("seleccione una operacion")
print("1.suma")
print("2.resta")
print("3.divicion")
opcion=float(input("ingresar una operacion:"))
n1=float(input("ingresar 1n°:"))
n2=float(input("ingresar 2n°:"))
if opcion==1:
     total=n1+n2
     print("el resultado es:",total)
elif opcion==2:
     total=n1-n2
     print("el resultado es:",total)
else:
     total=n1/n2
     print("el resultado es:",total)