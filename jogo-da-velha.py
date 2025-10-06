# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)

# Função para verificar se há um vencedor
def verificar_vitoria(tabuleiro):
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != " ":
            return linha[0]
    
    # Verificar colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[0][col] != " ":
            return tabuleiro[0][col]
    
    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ":
        return tabuleiro[0][2]
    
    return None

# Função para verificar se o tabuleiro está cheio
def tabuleiro_cheio(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

# Função principal para o jogo
def jogo_da_velha():
    # Inicializar o tabuleiro 3x3
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    
    jogador_atual = "X"
    
    while True:
        exibir_tabuleiro(tabuleiro)
        
        # Pedir ao jogador para escolher a linha e a coluna
        print(f"Jogador {jogador_atual}, escolha uma linha (0, 1, 2) e uma coluna (0, 1, 2):")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        
        # Validar se a posição está livre
        if tabuleiro[linha][coluna] != " ":
            print("Esta posição já está ocupada! Tente novamente.")
            continue
        
        # Fazer a jogada
        tabuleiro[linha][coluna] = jogador_atual
        
        # Verificar se há um vencedor
        vencedor = verificar_vitoria(tabuleiro)
        if vencedor:
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {vencedor} venceu!")
            break
        
        # Verificar se houve empate
        if tabuleiro_cheio(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break
        
        # Alternar entre os jogadores
        jogador_atual = "O" if jogador_atual == "X" else "X"

# Iniciar o jogo
jogo_da_velha()
