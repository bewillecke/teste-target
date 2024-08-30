def pertence_fibonacci(n):
    # Inicializando os primeiros valores da sequência de Fibonacci
    a, b = 0, 1
    
    # Gera a sequência de Fibonacci até que o número seja maior ou igual ao número informado
    while a < n:
        a, b = b, a + b
    
    # Verifica se o número está na sequência
    return a == n

# Solicitando ao usuário que informe um número
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verificando se o número pertence à sequência de Fibonacci e exibindo o resultado
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")