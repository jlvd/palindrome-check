import random

salida = False
a=1
#PRuebas reversando cadenas
'''
prueba="1234567890"
print(f"Prueba: {prueba[0:4:2]}")

print(f"Prueba reversa: {prueba[4:0:-2]}")
'''
while not salida:
    numero = str(random.randint(1000, 9999))
    if numero == numero[::-1]:
        print(f"Terminamos!!! \nHemos encontrado un palíndromo: {numero} en solo {a} intentos.")
        salida = True
    a += 1
