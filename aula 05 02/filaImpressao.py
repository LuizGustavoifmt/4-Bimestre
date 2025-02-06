class FilaDeImpressao:
    # Método para configurar a fila de impressão inicial
    def configurar_inicial(self):
        self.fila = []  # Inicializa a fila como uma lista vazia

    # Método para adicionar um trabalho à fila
    def adicionar_trabalho(self, trabalho):
        self.fila.append(trabalho)  # Adiciona o trabalho à fila
        print(f"Trabalho '{trabalho}' adicionado à fila de impressão.")  # Exibe mensagem de confirmação

    # Método para processar (imprimir) o próximo trabalho na fila
    def processar_trabalho(self):
        if not self.esta_vazia():  # Verifica se a fila não está vazia
            trabalho = self.fila.pop(0)  # Remove e obtém o primeiro trabalho da fila
            print(f"Imprimindo trabalho '{trabalho}'...")  # Exibe mensagem de impressão

    # Método para mostrar os trabalhos na fila
    def mostrar_trabalho(self):
        if self.esta_vazia():  # Verifica se a fila está vazia
            print("Fila de impressão vazia.")  # Exibe mensagem se a fila estiver vazia
        else:
            print("Fila de impressão atual:")  # Exibe cabeçalho da lista de trabalhos
            for trabalho in self.fila:  # Itera sobre os trabalhos na fila
                print(f"- {trabalho}")  # Exibe cada trabalho na fila

    # Método para verificar se a fila está vazia
    def esta_vazia(self):
        return len(self.fila) == 0  # Retorna True se a fila estiver vazia, caso contrário, False

# Função para exibir o menu e gerenciar a interação do usuário
def menu():
    fila_impressao = FilaDeImpressao()  # Cria uma nova instância da fila de impressão
    fila_impressao.configurar_inicial()  # Configura a fila de impressão inicial
    while True:  # Loop infinito para manter o menu ativo
        print("Opções:")  # Exibe as opções do menu
        print("1 - Adicionar um trabalho na fila de impressão")
        print("2 - Imprimir o próximo trabalho da fila")
        print("3 - Mostrar a fila de impressão")
        print("4 - Sair")
        escolha = input("Digite a opção de 1 a 4: ")  # Solicita a escolha do usuário
        
        if escolha == "1":  # Se o usuário escolher adicionar um trabalho
            trabalho = input("Digite o nome do trabalho a ser impresso: ")  # Solicita o nome do trabalho
            fila_impressao.adicionar_trabalho(trabalho)  # Adiciona o trabalho à fila
        elif escolha == "2":  # Se o usuário escolher imprimir um trabalho
            fila_impressao.processar_trabalho()  # Processa (imprime) o próximo trabalho
        elif escolha == "3":  # Se o usuário escolher mostrar a fila
            fila_impressao.mostrar_trabalho()  # Exibe os trabalhos na fila
        elif escolha == "4":  # Se o usuário escolher sair
            print("Saindo...")  # Exibe mensagem de saída
            break  # Encerra o loop
        else:  # Se a opção escolhida for inválida
            print("Opção inválida! Tente novamente.")  # Exibe mensagem de erro

# Para executar o menu quando o script é executado diretamente
if __name__ == "__main__":
    menu()  # Chama a função menu para iniciar a interação