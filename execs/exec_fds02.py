# # ========================================================
# # PARTE 2 - EXERCÍCIOS DE CORREÇÃO DE ERROS (5 exercícios)
# # ========================================================
# # Cada código abaixo tem ERROS. Identifique e corrija.

# # -----------------------------------------------------
# # ERRO 1 - Erro de tipo
# # -----------------------------------------------------

# idade = input("Digite sua idade: ")
# print("Daqui a 10 anos você terá", int(idade) + 10, "anos")


# # -----------------------------------------------------
# # ERRO 2 - Nome de variável inválido
# # -----------------------------------------------------

nome = input("Digite seu nome: ")
print(f"seu nome e {nome}")


# # -----------------------------------------------------
# # ERRO 3 - Erro de conversão e impressão
# # -----------------------------------------------------

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso / (altura * altura)
print(f"Seu IMC e: {imc:.2f}")


# # -----------------------------------------------------
# # ERRO 4 - Uso errado do f-string
# # -----------------------------------------------------

nome = "Carlos"
idade = 25
print(f"Meu nome é {nome}, e tenho {idade} anos")


# # -----------------------------------------------------
# # ERRO 5 - Múltiplos erros
# # -----------------------------------------------------

print("=== CALCULADORA ===")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
print(f"A soma e: {num1 + num2}")
print(f"A média é: {(num1 + num2) / 12}")