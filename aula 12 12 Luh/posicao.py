# Inicializa uma lista vazia para armazenar os valores
valores = []

# Lê 10 valores do usuário
for i in range(10):
    valor = float(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

# Inicializa variáveis para armazenar o maior valor e sua posição
maior_valor = valores[0]
posicao_maior = 0

# Percorre a lista para encontrar o maior valor e sua posição
for i in range(1, len(valores)):
    if valores[i] > maior_valor:
        maior_valor = valores[i]
        posicao_maior = i

# Exibe o maior valor e sua posição
print(f"O maior valor é {maior_valor} e está na posição {posicao_maior}.")