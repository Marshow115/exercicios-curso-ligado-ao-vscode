#contagem de vogais e consoantes, escreva um programa que conte o número de vogais e consoantes em uma string.


#receber o texto para contar as vogais

texto = input("digite o texto:")
vogais = 0
consoantes = 0
for caractere in texto:
    if caractere.lower()in "aeiou":

       vogais += 1
    elif caractere.lower()in "bcdfghjklmnpqrstvxwyz":
       consoantes +=1
print(f"número de vogais: {vogais}")
print(f"número de consoantes: {consoantes}")
