# Inicializa uma lista vazia para armazenar as notas dos alunos
nota = []

# Loop que irá repetir 5 vezes para coletar as notas de 5 alunos
for i in range(5):
    # Solicita ao usuário que digite a nota do aluno e converte para float
    nota_aluno = float(input("DIGITE A NOTA DO ALUNO: "))
    # Adiciona a nota do aluno à lista de notas
    nota.append(nota_aluno)

# Inicializa a variável media com valor 0 (essa variável está sendo usada para calcular a média)
media = 0

# Loop que irá somar todas as notas na lista
for no in nota:
    # Adiciona a nota atual à variável media
    media += no 

# Calcula a média dividindo a soma das notas pelo número de alunos (5)
media = media / 5

# Imprime a média dos alunos após cada nota ser adicionada
print("A MÉDIA DOS ALUNOS É: ", media)