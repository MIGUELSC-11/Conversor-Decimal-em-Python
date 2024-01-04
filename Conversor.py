def decimal_para_binario (decimal):
    return bin(decimal)

def decimal_para_octal (decimal):
    return oct(decimal)

def decimal_para_hexa (decimal):
    return hex(decimal)

num = int(input("Digite o numero em decimal: "))
print("Escolha para qual base deseja converter: ")
print("Opção 1: Binario")
print("Opção 2: Octal")
print("Opção 3: Hexadecimal")

opcao = int(input("Ecolha qual opcão deseja converter: "))
if opcao == 1:
    resultado = decimal_para_binario(num)
    print("O numero decimal", num, "em binario é: " f'{num:b}')
elif opcao == 2:
    resultado = decimal_para_octal(num)
    print("O numero em decimal", num, "em octal é: " f'{num:o}')
elif opcao == 3:
    resultado = decimal_para_hexa(num)
    print("O numero em decimal", num, "em hexa é: "f'{num:x}')
else:
    print("Digite uma variavel aceitavel 1, 2 ou 3")