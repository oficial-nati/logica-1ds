 #Contagem dos dias até o fim de semana
dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", 
        "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

print("Contagem dos dias até o fim de semana:\n")
for i in range(5):  # até a sexta-feira
    print(dias[i])

print("\nChegou o fim de semana! 🎉")

# Lista com os preços dos itens da compra
precos = [10.50, 23.75, 5.90, 12.30, 4.99]

# Variável para armazenar o total da compra
total = 0

# Loop for para somar os preços
for preco in precos:
    total += preco

# Exibir o total da compra
print(f"O total da compra é: R${total:.2f}")

# Simulando mensagens no celular
mensagens = ["Oi, tudo bem?", "Você vai na festa hoje?", "Vamos sair mais tarde?", "Nada de novo por aqui."]
mensagens_vistas = []

# Função para simular a resposta às mensagens
def responder(mensagem):
    print(f"Respondendo: '{mensagem}'")
    mensagens_vistas.append(mensagem)

# Simulando o processo de conferir e responder até não haver mais mensagens
while mensagens:
    mensagem = mensagens.pop(0)  # Pega a primeira mensagem da lista
    print(f"Nova mensagem: '{mensagem}'")
    responder(mensagem)  # Responde à mensagem

print("Todas as mensagens foram respondidas!") 

# Definir o valor total e o valor economizado por semana
valor_total = 100
economia_semanal = 10

# Inicializar variáveis
total_economizado = 0
semanas = 0

# Loop enquanto o total economizado for menor que o valor total
while total_economizado < valor_total:
    total_economizado += economia_semanal
    semanas += 1

# Exibir o resultado
print(f"Você precisará de {semanas} semanas para economizar R$ {valor_total}.") 

# Lista de alunos presentes
lista_presenca = ["João", "Maria", "Ana", "Pedro", "Carlos"]

# Nome do aluno a ser buscado
aluno_buscado = "Ana"

# Verificar se o aluno está na lista de presença
for aluno in lista_presenca:
    if aluno == aluno_buscado:
        print(f"O aluno {aluno_buscado} está presente na sala.")
        break
else:
    print(f"O aluno {aluno_buscado} não está presente na sala.") 
