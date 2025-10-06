import time

# Definir a senha fixa
senha_fixa = "1234"

# Função principal do sistema de login
def sistema_login():
    tentativas = 3  # Número de tentativas
    tempo_limite = 30  # Tempo limite de 30 segundos
    inicio = time.time()  # Iniciar o contador de tempo

    while tentativas > 0:
        # Calcular o tempo decorrido
        tempo_decorrido = time.time() - inicio

        # Verificar se o tempo expirou
        if tempo_decorrido > tempo_limite:
            print("Tempo expirado. Acesso negado.")
            break
        
        # Solicitar a senha
        senha = input(f"Tentativas restantes: {tentativas}. Digite a senha: ")

        # Verificar se a senha está correta
        if senha == senha_fixa:
            print("Acesso permitido!")
            break
        else:
            tentativas -= 1  # Reduzir o número de tentativas
            if tentativas > 0:
                print(f"Senha incorreta! Você ainda tem {tentativas} tentativas.")
            else:
                print("Número de tentativas esgotado. Acesso negado.")

# Chamar a função para executar o sistema de login
sistema_login()
