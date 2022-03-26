texto = input("¿En que estas pensando?\n")
n = 1

for c in texto:
    if c==" ":
        n+=1
print(f'Gracias por compartir tus pensamientos en {n} palabras.')
