import random

# Lista de palavras para o jogo
palavras = ["python", "java", "javascript", "forca", "computador", "desenvolvimento"]

# Função para exibir o desenho do boneco com base no número de erros
def exibir_boneco(erros):
    bonecos = [
        """
        ------
        |    |
             |
             |
             |
             |
             |
        -----|-----""",
        
        """
        ------
        |    |
        O    |
             |
             |
             |
             |
        -----|-----""",
        
        """
        ------
        |    |
        O    |
        |    |
             |
             |
             |
  ------
        |    |
        O    |
       /|    |
             |
             |
             |
        -----|-----""",
        
        """
        ------
        |    |
        O    |
       /|\\   |
             |
             |
             |
        -----|-----""",
        
        """
        ------
        |    |
        O    |
       /|\\   |
       /     |
             |
             |
        -----|-----""",
        
        """
        ------
        |    |
        O    |
       /|\\   |
       / \\   |
             |
             |
        -----|-----"""
    ]
    print(bonecos[erros])

# Função principal do jogo da forca
def jogo_da_forca():
    palavra = random.choice(palavras)  # Escolher uma palavra aleatória
    letras_corretas = ["_"] * len(palavra)  # Iniciar as letras corretas como underscores
    letras_erradas = []  # Lista para armazenar as letras erradas
    erros = 0  # Contador de erros

    print("Bem-vindo ao jogo da Forca!")
    
    while erros < 6:  # O jogador tem no máximo 6 erros
        # Exibir o estado atual do boneco
        exibir_boneco(erros)
        
        # Exibir as letras corretas e as erradas
        print("Palavra: " + " ".join(letras_corretas))
        print("Letras erradas: " + ", ".join(letras_erradas))
        
        # Solicitar a letra do jogador
        letra = input("Digite uma letra: ").lower()

        # Validar 
