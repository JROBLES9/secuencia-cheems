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
newWords = []
for word in cheems:
    #separar la palabra por la cantidad de letras de secuencia[i][j]
    grupo = []
    newWord = []
    sumatoria = 0
    for j in secuencias[cheems.index(word)]:
        #separar cada word en rangos de 0 a j1 y j1 a j2 y j2 a jn hasta que se acaben las letras
        if sumatoria < len(word):
            grupo.append(word[sumatoria:sumatoria+j])
        else:
            break
        sumatoria += j
    
    for j in secuencias[cheems.index(word)]:
        #indice j en secuencias[cheems.index(word)]
        indice = secuencias[cheems.index(word)].index(j)
        newWord.append(chr(ord(word[indice]) + j))

    #convertir newWord en string
    newWord = ''.join(newWord)
    newWords.append(newWord)
print(newWords)

#4. convertimos en octal
octal = []
for word in newWords:

    octal.append(''.join(str(oct(ord(i))).lstrip("0o") for i in word))
print(octal)
#5. remplazamos 0 por 9 y 7 por 8
#6. convertimos a letras


