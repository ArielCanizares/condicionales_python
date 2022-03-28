# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1 > texto_2:
    print(texto_1,"es mayor alfabéticamente que",texto_2,".")
else:
    print(texto_2,"es mayor alfabéticamente que",texto_1,".")

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1)> len(texto_2):
    print("La palabra",texto_1,"tiene mayor cantidad de letras.")
else:
    print("La palabra",texto_2,"tiene mayor cantidad de letras.")

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda
if texto_1[0] > texto_2[0]:
    print("La primera letra de",texto_1, "es mayor a la primera letra de",texto_2,".")
elif texto_1[0] == texto_2[0]:
    print("La primer letra de", texto_1,"y la primera de",texto_2,"son las mismas.")
else:
    print("La primera letra de",texto_1, "no es mayor a la primer letra de",texto_2,".")

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if copia_texto_1 == texto_1:
    print("La palabra", copia_texto_1,"es igual a",texto_1,".")
else:
    print("La palabra", copia_texto_1,"y",texto_1,"son distintas.")

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
if copia_texto_1 != texto_2:
    print("La palabra", copia_texto_1,"es distinta a",texto_2,".")
else:
    print("La palabra", copia_texto_1,"es igual a", texto_2,".")