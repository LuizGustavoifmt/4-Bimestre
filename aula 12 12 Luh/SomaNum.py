# Inicializa uma lista vazia para armazenar os números
numeros = []

# Lê 10 números reais
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Inicializa variáveis para soma dos positivos e contagem dos negativos
soma_positivos = 0
quantidade_negativos = 0

# Processa a lista de números
for numero in numeros:
    if numero > 0:
        soma_positivos += numero
    elif numero < 0:
        quantidade_negativos += 1

# Exibe os resultados
print(f"Soma dos números positivos: {soma_positivos}")
print(f"Quantidade de números negativos: {quantidade_negativos}")