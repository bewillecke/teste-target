import json

# Função para calcular o menor, maior e número de dias com faturamento superior à média
def processar_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    
    faturamentos = [item['valor'] for item in dados['faturamento_diario'] if item['valor'] > 0]
    
    if not faturamentos:
        return {
            "menor_faturamento": None,
            "maior_faturamento": None,
            "dias_acima_da_media": 0
        }
    
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_mensal = sum(faturamentos) / len(faturamentos)
    dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)
    
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }

# Caminho do arquivo JSON
caminho_arquivo = 'faturamento.json'

resultados = processar_faturamento(caminho_arquivo)

print(f"Menor valor de faturamento: R${resultados['menor_faturamento']:.2f}")
print(f"Maior valor de faturamento: R${resultados['maior_faturamento']:.2f}")
print(f"Número de dias com faturamento acima da média: {resultados['dias_acima_da_media']}")