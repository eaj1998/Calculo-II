import numpy as np

# Função para ser integrada
def f(x):
    return np.exp(-x) + 1

# Regra dos Trapézios
def trapezoidal_rule(a, b, n, f=f):
    # Tamanho dos subintervalos
    h = (b - a) / n
    # Soma dos valores de f(x) nos subintervalos
    result = 0.5 * (f(a) + f(b))  # Inicia com os extremos a e b
    for i in range(1, n):
        x_i = a + i * h
        result += f(x_i)
    result *= h
    return result

# Parâmetros de entrada
def calculate_area(a, b, n):
    area = trapezoidal_rule(a, b, n)
    return area

# Função principal para rodar o cálculo com valores fixos de n
def main():
    a = float(input("Digite o valor de a (limite inferior): "))
    b = float(input("Digite o valor de b (limite superior): "))
    print("Escolha o número de subintervalos:")
    print("1. n = 4")
    print("2. n = 10")
    print("3. n = 50")
    option = int(input("Digite a opção (1, 2 ou 3): "))
    
    if option == 1:
        n = 4
    elif option == 2:
        n = 10
    elif option == 3:
        n = 50
    else:
        print("Opção inválida, usando n = 4 por padrão.")
        n = 4
    
    # Calcular a área aproximada
    area = calculate_area(a, b, n)
    print(f"A aproximação da área sob a curva no intervalo [{a}, {b}] com n = {n} subintervalos é: {area:.6f}")

# Executar a função principal
if __name__ == "__main__":
    main()