nomeDoUsuario = input("Digite seu nome: ")
anoDeNascimento = int(input("Digite seu ano de nascimento: "))

idadeAtual = 2024 - anoDeNascimento
idadeDaqui4Anos = idadeAtual + 4 

print(f"\tOlá\n\t{nomeDoUsuario}\n\tvc tem \n\t{idadeAtual} anos\n e daqui a 4 anos terá {idadeDaqui4Anos} anos.")
