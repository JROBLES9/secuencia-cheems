def secuencia(word):
    secuencia = []
    for n in range(0, len(word)):
        secuencia.append((((n+2)*8)%5))
    return secuencia
#1. convertimos en cheems y hallamos n
#recibir una entrada
words = input()

#separamos words por palabras
words = words.split()
print(words)

#convertir en cheems, si la palabra tiene r colocar antes m de la r en la palabra, si no tiene r colocar m al final de la palabra
cheems = []
for i in words:
    if 'r' in i:
        i = i.replace('r', 'mr')
    else:
        i = i + 'm'
    cheems.append(i)
print(cheems)
#2.  aplicamos la secuencia

#para cada palabra aplicamos secuencia
secuencias = []
for i in cheems:
    secuencias.append(secuencia(i))
print(secuencias)



#3. aplicamos los grupos
#4. convertimos en octal
#5. remplazamos 0 por 9
#6. convertimos a letras


