import pandas as pd
import requests
import io

# IDs das planilhas no Google Sheets
sheets = {
    "liquidacao": "1aOztWaK6N07CWHCO-73YjhwcgLlFvNHN3s02Nii1Zwg",
    "custas": "1cWMPOn27XkzhQ84uff2RxGyrkYc2-yeTPStOUf2Exf4"
}

# Nome da aba que queremos baixar
aba = "CONSOLIDACAO"

# Função para baixar e salvar a aba específica
def baixar_e_salvar(nome, sheet_id, aba):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={aba}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na requisição

        # Tenta decodificar o CSV corretamente
        csv_data = response.content.decode("utf-8", errors="replace")

        # Converte para um DataFrame Pandas
        df = pd.read_csv(io.StringIO(csv_data))

        print(f"Dados de {nome} ({aba}) carregados com sucesso!")
        print(df.head())  # Exibe as primeiras linhas para conferência

        # Salvando como CSV
        df.to_csv(f"{nome}.csv", index=False, encoding="utf-8")

        print(f"Arquivo {nome}.csv salvo com sucesso!\n")
    except Exception as e:
        print(f"Erro ao carregar {nome}: {e}")

# Baixando e salvando os arquivos
for nome, sheet_id in sheets.items():
    baixar_e_salvar(nome, sheet_id, aba)
