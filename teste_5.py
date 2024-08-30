def inverter_string(s):
    # Cria uma lista para armazenar os caracteres invertidos
    lista_invertida = []
    
    # Itera sobre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        lista_invertida.append(s[i])
    
    # Converte a lista de volta para uma string
    return ''.join(lista_invertida)

# Solicita ao usuário que informe a string
string_original = input("Informe a string para inverter: ")

# Inverte a string e exibe o resultado
string_invertida = inverter_string(string_original)
print(f"String invertida: {string_invertida}")