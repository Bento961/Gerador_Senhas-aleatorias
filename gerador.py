import string
import random

letras_min = string.ascii_lowercase
letras_mai = string.ascii_uppercase
num = string.digits
caracteres_esp = "@#$%&^*()!"

todos_caracteres = letras_mai + letras_min + num + caracteres_esp

# Pergunta ao usuário o tamanho desejado da senha
tamanho = int(input("Digite o tamanho da senha que você deseja gerar: "))

continua = "s"
while continua == "s":
    senha = "".join(random.sample(todos_caracteres, tamanho))
    print(f"Senha gerada: {senha}")

    continua = input("Deseja gerar outra senha? (s/n): ").lower()
