#1. convertimos en cheems y hallamos n
#recibir una entrada
words = input()

#separamos words por palabras
n = len(words)
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
#3. aplicamos los grupos
#4. convertimos en octal
#5. remplazamos 0 por 9
#6. convertimos a letras

