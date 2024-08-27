# Gerador de Senhas Aleatórias

Este é um simples gerador de senhas aleatórias escrito em Python. Ele permite que o usuário especifique o tamanho da senha e gera uma senha contendo letras maiúsculas, 
letras minúsculas, números e caracteres especiais.

## Como Usar

1. Clone este repositório para o seu ambiente local.
2. Execute o script `senha_aleatoria.py`.
3. Insira o tamanho desejado para a senha quando solicitado.
4. O script gerará e exibirá uma senha aleatória.
5. Você pode optar por gerar outra senha ou encerrar o programa.

## Exemplo de Uso

```python
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
