print("=== SISTEMA DE ESTACIONAMENTO ===")
placa = input("Digite a placa do veículo: ")
horas = int(input("Digite o tempo de permanência (em horas): "))

if horas <= 1:
    valor = 8.00
elif horas <= 3:
    valor = 15.00
else:
    valor = 20.00

print(f"\nVeículo de placa {placa}: Total a pagar = R$ {valor:.2f}")
