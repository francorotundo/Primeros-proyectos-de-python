nombre = input("¿Cual es el nombre de tu Empresa?\n")

nombre=nombre.title()
a = nombre[0]
for i,ch in enumerate(nombre):
    if ch==" ":
        a+=(nombre[i+1])

print(a)