#nesse exercicio darei continuidade aos exercicios feitos no colab e no curso

#bom... vou tentar refazer um exercicio aq q se trata de criar uma lista e fazer com que o codgo releia e saiba qual o numero mais se repete

##meu codigo ficou assim:
lista = [8, 3, 5, 8, 2, 3, 8, 4, 5, 8, 1]
frequencia ={}


for numero in lista:
        if numero in frequencia:
                frequencia[numero] +=1
        else:
                frequencia[numero] = 1

numero_frequente = lista[0]
for numero, quantidade in frequencia.items():
        if quantidade > frequencia[numero_frequente]:
                numero_frequente = numero

print(f'O numero escolhido foi {numero_frequente}.')


##copilot fez ele rodar o loop de novo assim
# Confere o resultado contando novamente o numero escolhido.


quantidade_conferida = 0
for numero in lista:
        if numero == numero_frequente:
                quantidade_conferida += 1

if quantidade_conferida == frequencia[numero_frequente]:
        print('A conferência confirmou que o resultado está certo.')
else:
        print('A conferência encontrou um erro no resultado.')
            