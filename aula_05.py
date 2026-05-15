name_complete = input("Digite seu nome completo: ")

print(f"Quantidade de Letras (sem espaços): {len(name_complete.replace (' ', ''))}")
print(f"Nome em Maiusculo: {name_complete.upper()}")
print(f"Nome em minusculo: {name_complete.lower()}")
print(f"Primeira letra: {name_complete[0]}")
print(f"Ultima letra: {name_complete[-1]}")
print(f"Nome invertido: {name_complete[::-1]}")