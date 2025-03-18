import pandas as pd
import gdown

# IDs dos arquivos no Google Drive
#liquidacao_id = "1cWMPOn27XkzhQ84uff2RxGyrkYc2-yeTPStOUf2Exf4"
custas_id = "1aOztWaK6N07CWHCO-73YjhwcgLlFvNHN3s02Nii1Zwg"

# URLs dos arquivos no Google Drive
#liquidacao_url = f"https://drive.google.com/uc?id={liquidacao_id}"
custas_url = f"https://drive.google.com/uc?id={custas_id}"

# Caminhos para salvar os arquivos localmente
#liquidacao_path = "Central_de_Contadoria_TJPE_Liquidacao.csv"
custas_path = "Central_de_Contadoria_TJPE_Custas.csv"

# Fazer o download dos arquivos
print("Baixando arquivos do Google Drive...")
#gdown.download(liquidacao_url, liquidacao_path, quiet=False)
gdown.download(custas_url, custas_path, quiet=False)
print("Download concluído.")

# Carregar os arquivos
#liquidacao = pd.read_csv(liquidacao_path)
custas = pd.read_csv(custas_path)

# Continue com as etapas do código original...
# Por exemplo:
#print(f"Arquivo de liquidação carregado: {liquidacao.shape[0]} linhas")
print(f"Arquivo de custas carregado: {custas.shape[0]} linhas")

# O restante do código continua aqui...
