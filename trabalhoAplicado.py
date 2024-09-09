import numpy as np

# Função f(x) definida conforme a observação
def f(x):
    return np.exp(-x) + 1

def trapezio(a, b, n):
    """
    Calcula a aproximação da área sob a curva y=f(x) no intervalo [a, b]
    usando o método dos trapézios com n subintervalos.
    
    :param a: Limite inferior do intervalo.
    :param b: Limite superior do intervalo.
    :param n: Número de subintervalos.
    :return: Aproximação da área.
    """
    # Comprimento de cada subintervalo
    h = (b - a) / n
    
    # Calcula a soma dos valores de f nos extremos
    soma = (f(a) + f(b)) / 2
    
    # Adiciona a soma dos valores de f nos pontos internos
    for i in range(1, n):
        xi = a + i * h
        soma += f(xi)
    
    # Multiplica pela largura do intervalo e retorna a área aproximada
    return soma * h

def main():
    # Solicita a entrada do usuário
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    n = int(input("Digite o número de subintervalos (4, 10, 50 ou outro): "))
    
    # Verifica se o número de subintervalos é válido
    if n <= 0:
        print("Número de subintervalos deve ser positivo.")
        return
    
    # Calcula a área aproximada usando o método dos trapézios
    area_aproximada = trapezio(a, b, n)
    
    # Exibe o resultado
    print(f"Aproximação da área sob a curva y=f(x) no intervalo [{a}, {b}] com {n} subintervalos: {area_aproximada:.6f}")

if __name__ == "__main__":
    main()
