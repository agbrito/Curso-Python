# =============================================================
# EXERCÍCIOS - AULAS 1, 2 e 3 (input, print, variáveis e tipos)
# =============================================================

# ===============================================
# PARTE 1 - EXERCÍCIOS DE CRIAÇÃO (10 exercícios)
# ===============================================

# -----------------------------------------------------
# EXERCÍCIO 1 - Apresentação pessoal
# -----------------------------------------------------
# Crie um programa que armazene seu nome, idade e cidade em variáveis 
# e depois exiba.

# name = "Angelo"
# age = 18
# city = "Acarau"

# print(f"Nome: {name} \n idade: {age} \n Cidade: {city}")

# -----------------------------------------------------
# EXERCÍCIO 2 - Cadastro de produto
# -----------------------------------------------------
# Solicite ao usuário o nome do produto, o preço e a quantidade em estoque. 
# Depois exiba.

# name_product = input("Nome do produto:")
# price_product = float(input("Preço do produto: (R$)"))
# quantity_product = int(input("Quantidade em estoque: "))

# print(f"Produto: {name_product} ")
# print(f"Preço: R$ {price_product:.2f}")
# print(f"Quatidade em estoque: {quantity_product}")

# -----------------------------------------------------
# EXERCÍCIO 3 - Conversor de idade para meses e dias
# -----------------------------------------------------
# Peça a idade do usuário em anos e calcule:
# - Quantos meses de vida , dica: (idade * 12)
# - Quantos dias aproximados, dica: (idade * 365)
# Exiba os resultados.

# age_years = int(input("Digite sua idade em anos: "))
# age_months = age_years * 12
# age_days = age_years * 365

# print(f"Vc tem aproximadamente {age_months} meses de vida.")
# print (f"Vc tem aproximadamente {age_days} dias de vida.")

# -----------------------------------------------------
# EXERCÍCIO 4 - Refeitório da faculdade
# -----------------------------------------------------
# Solicite o nome do aluno, quantas refeições ele fez no dia e o valor 
# de cada refeição. Calcule o total gasto no dia e exiba.

name_estudent = input("Nome do aluno: ")
quantity_meals = int(input("Quantas refeições fez no dia? "))
price_meal = float(input("Valor de cada refeição: R$ "))
total_spent = quantity_meals * price_meal

print(f"Total gasto no dia: R$ {total_spent:.2f}")

# -----------------------------------------------------
# EXERCÍCIO 5 - Dados do retângulo
# -----------------------------------------------------
# Peça a largura e a altura de um retângulo (números decimais). 
# Calcule e mostre:
# - A área , dica: (largura * altura)
# - O perímetro,  dica: (largura + altura) * 2

length_rectangle = float(input("Largura do retangulo: "))
height_rectangle = float(input("Altura do retangulo: "))

area_rectangle = length_rectangle * height_rectangle
perimeter_rectangle = (length_rectangle + height_rectangle) * 2

print(f"Area do retangulo: {area_rectangle:.2f}")
print(f"Perimetro do retangulo: {perimeter_rectangle:.2f}")

# -----------------------------------------------------
# EXERCÍCIO 6 - Média de 3 notas
# -----------------------------------------------------
# Solicite 3 notas de um aluno (valores decimais). 
# Calcule a média aritmética e exiba.

grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))
grade3 = float(input("Digite a terceira nota: "))

average_grade = (grade1 + grade2 + grade3) / 3

print(f"A media das notas é: {average_grade:.2f}")

# -----------------------------------------------------
# EXERCÍCIO 7 - Dados pessoais formatados
# -----------------------------------------------------
# Solicite nome completo, telefone, e-mail e ano de nascimento. 
# Exiba tudo em uma única linha, separado por " | " 
# Dica: (use o parâmetro sep ou f-string).

name_full = input("Nome completo: ")
phone = input("Telefone: ")
email = input("E-mail: ")
year_birth = int(input("Ano de nascimento: "))

print(f"{name_full} | {phone} | {email} | {year_birth}")

# -----------------------------------------------------
# EXERCÍCIO 8 - Tempo de estudo
# -----------------------------------------------------
# Pergunte ao usuário quantos minutos ele estuda por dia. Converta e mostre:
# - Quantas horas isso representa, dica: (minutos / 60)
# - Quantos segundos (minutos * 60)

minutes_study = int(input("Quantos minutos vc estuda por dia? "))
hours_study = minutes_study / 60
seconds_study = minutes_study * 60

print(f"Tempo de estudo em horas: {hours_study:.2f}")
print(f"Tempo de estudo em segundos: {seconds_study:.2f}")
# -----------------------------------------------------
# EXERCÍCIO 9 - Troca de valores
# -----------------------------------------------------
# Crie duas variáveis: a = 10 e b = 99. Depois troque os valores entre elas 
# (faça com que "a" receba 99 e "b" receba 10) usando apenas variáveis temporárias 
# ou outro método (simples). Exiba os valores antes e depois da troca.

a = 10
b = 99

print(f"Antes da troca: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"Depois da troca: a = {a}, b = {b}")
# -----------------------------------------------------
# EXERCÍCIO 10 - Salário calculado
# -----------------------------------------------------
# Solicite o valor do salário por hora e a quantidade de horas trabalhadas 
# no mês. Calcule o salário total do mês e exiba:

# Dicas:
# Salário por hora: R$ [valor]
# Horas trabalhadas: [horas]
# Salário do mês: R$ [total]

salary_per_hour = float(input("Valore do salario por hora: R$ "))
hours_worked = int(input("Quantidade de horas trabalhadas no mes: "))
total_salary = salary_per_hour * hours_worked

print(f"Salario por hora: R$ {salary_per_hour:.2f}")
print(f"Horas trabalhadas: {hours_worked}")
print(f"Salario do mes: R$ {total_salary:.2f}")