def secuencia(word):
    secuencia = []
    for n in range(1, len(word)+1):
        secuencia.append((((n*8)+2)%5))
    return secuencia


# 1. Tomar el input del usuario
letras = input("Por favor, introduce las letras: ")

letras = letras.split()

# 3. Convertir las letras a números
numeros = []
for letra in letras:
    numeros.append(''.join(str(ord(i) - 97) for i in letras))
print(numeros)

# 4. Reemplazar '0' por '9' y '7' por '8'
octales = []
for numero in numeros:
    octales.append(numeros.replace('9', '0').replace('8', '7'))
print(octales)

# 5. agregar 0o cada 3 digitos de octal
nonales = []
for octal in octales:
    nonal = []
    for i in range(0, len(octal), 3):
        nonal.append('0o' + octal[i:i+3])
    nonales.append(nonal)
print(nonal)

#convertir de octal a string
palabras = []
for nonal in nonales:
    palabra = []
    for i in nonal:
        palabra.append(chr(int(i, 8)))
    palabras.append(palabra)

#unir todo en un string
palabrasUnidas = []
for palabra in palabras:
    palabraUnida = ''.join(palabra)
    palabrasUnidas.append(palabra)
print(palabras)

#hallar secuencia de la entrada
secuencias = []
for palabraUnida in palabrasUnidas:
    secuencia = []
    for n in range(1, len(palabraUnida)+1):
        secuencia.append((((n*8)+2)%5))
    secuencias.append(secuencia)
print(secuencias)

#aplicar los grupos
newWords = []
#for word in palabras:
    #separar la palabra por la cantidad de letras de secuencia[i][j]
for palabraUnida in palabrasUnidas:
    grupo = []
    newWord = []
    sumatoria = 0
    for j in secuencia:
        #separar cada word en rangos de 0 a j1 y j1 a j2 y j2 a jn hasta que se acaben las letras
        if sumatoria < len(palabrasUnidas):
            grupo.append(palabras[sumatoria:sumatoria+j])
        else:
            break
        sumatoria += j

    for j in secuencia:
        #indice j en secuencias[cheems.index(word)]
        indice = secuencia.index(j)
        newWord.append(chr(ord(palabras[indice]) - j))

    #convertir newWord en string
    newWord = ''.join(newWord)
    newWords.append(newWord)

# 6. Cambiar la posición de las letras según la secuencia
print(newWords)