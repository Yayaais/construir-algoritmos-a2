import datetime
import requests

def cotar():
    print("Iniciando consulta...")
    cotacoes = []
    hoje = datetime.date.today()

    for i in range(365):
        dia = hoje - datetime.timedelta(days=i)  # Volta um dia a cada repetição
        data = dia.strftime("%m-%d-%Y")  # Formata a data para a API

        url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$format=json"

        resposta = requests.get(url)  # Consulta a cotação
        dados = resposta.json()["value"]  # Pega os dados recebidos

        if dados:
            cotacoes.append(dados[0]["cotacaoCompra"])  # Guarda a cotação de compra

    return cotacoes

resultado = cotar()
print(resultado)
