import area
print("(1) Área do retângulo")
print("(2) Área do triângulo")
print("(3) Área do círculo")
escolha = int(input("Escolha: "))

if escolha == 1:
    lado = float(input("Digite lado: "))
    altura = float(input("Digite altura: "))
    resultado = area.area_retangulo(lado, altura)
    print(f"Resultado: {resultado:.2f}")
elif escolha == 2:
    lado = float(input("Digite lado: "))
    altura = float(input("Digite altura: "))
    resultado = area.area_triangulo(lado, altura)
    print(f"Resultado: {resultado:.2f}")
elif escolha == 3:
    raio = float(input("Digite raio: "))
    resultado = area.area_circunferencia(raio)
    print(f"Resultado: {resultado:.2f}")
else:
    print("Opção inválida")