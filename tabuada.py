#Criando um gerador de tabuadas com loop
numero = int(input("Digite um número para saber a tabuada: "))
contador = 1

print(30 * "-")
print("Tabuada de",numero)

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
print(30 * "-")
