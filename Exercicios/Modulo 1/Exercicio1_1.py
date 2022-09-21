from typing import List
import math


texto_claro ="acitalaeumsistemadecifrausadonaantigagrecia"
n=5


def ok(texto_claro , n):

    maxLetters = len(texto_claro )
    lettersPerLine = math.ceil(maxLetters/n)
    parts = [texto_claro [i:i+lettersPerLine] for i in range(0, len(texto_claro ), lettersPerLine)]

    def divideByLetter(word):
        return list(word)
    parts = list(map(divideByLetter,parts))
    
    texto_cifrado=""
    for i in range(lettersPerLine):
        for j in range(n):
            if len(parts[j])>i:
                letter=parts[j][i]
                texto_cifrado+=letter
    return texto_cifrado.upper()


print(ok(texto_claro , n))
