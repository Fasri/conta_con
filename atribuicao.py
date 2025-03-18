import pandas as pd

# Carregar os dados
def processar_tabela(arquivo_entrada, arquivo_saida):
    df = pd.read_excel(arquivo_entrada)
    
    # Garantir que 'Tempo na Contadoria' seja numérico
    df["Tempo na Contadoria"] = pd.to_numeric(df["Tempo na Contadoria"], errors='coerce')
    
    # Filtrar processos com mais de 15 dias e pendentes
    df_filtro = df[(df["Tempo na Contadoria"] > 15) & (df["Cumprimento"] == "Pendente")]
    
    #Filtrar processo com mais de 15 dias com o calculista e pendente
    df_filtro_calculista = df[(df["Tempo com o Contador"] > 15) & (df["Cumprimento"] == "Pendente")]

    # Dividir entre com e sem calculista
    df_sem_calculista = df_filtro[df_filtro["Calculista"].isna()]
    df_com_calculista = df_filtro_calculista[df_filtro_calculista["Calculista"].notna()]
    
    # Total de processos em cada aba
    df_total = pd.DataFrame({
        "Total": [len(df_sem_calculista), len(df_com_calculista)]
    }, index=["Sem Calculista", "Com Calculista"])

    # Criar o arquivo Excel com duas abas
    with pd.ExcelWriter(arquivo_saida) as writer:
        df_sem_calculista.to_excel(writer, sheet_name="Sem Calculista", index=False)
        df_com_calculista.to_excel(writer, sheet_name="Com Calculista", index=False)
        df_total.to_excel(writer, sheet_name="Resultado", index=False)
    
    print(f"Arquivo salvo como {arquivo_saida}")

# Exemplo de uso
processar_tabela(r"consolidacao.xlsx", "processos_filtrados.xlsx")
