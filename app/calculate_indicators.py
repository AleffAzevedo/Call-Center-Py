
import pandas as pd

def calculate_indicators(df):
    # Atendidas: Soma dos numeradores para 'Atendidas'
    df_atendidas = df[df["nome_indicador"] == "Atendidas"].groupby(["data", "atendente", "supervisor", "coordenador", "operacao", "cidade", "estado"]).agg(
        Atendidas=("numerador", "sum")
    ).reset_index()

    # TMA: Numerador (tempo total) / Denominador (chamadas atendidas)
    df_tma = df[df["nome_indicador"] == "TMA"].groupby(["data", "atendente", "supervisor", "coordenador", "operacao", "cidade", "estado"]).agg(
        numerador_tma=("numerador", "sum"),
        denominador_tma=("denominador", "sum")
    ).reset_index()
    df_tma["TMA"] = df_tma["numerador_tma"] / df_tma["denominador_tma"]
    df_tma = df_tma.drop(columns=["numerador_tma", "denominador_tma"])

    # CSAT: Numerador (soma das notas) / Denominador (total de pesquisas)
    df_csat = df[df["nome_indicador"] == "CSAT"].groupby(["data", "atendente", "supervisor", "coordenador", "operacao", "cidade", "estado"]).agg(
        numerador_csat=("numerador", "sum"),
        denominador_csat=("denominador", "sum")
    ).reset_index()
    df_csat["CSAT"] = df_csat["numerador_csat"] / df_csat["denominador_csat"]
    df_csat = df_csat.drop(columns=["numerador_csat", "denominador_csat"])

    # Unir os dataframes dos indicadores
    df_merged = df_atendidas.merge(df_tma, on=["data", "atendente", "supervisor", "coordenador", "operacao", "cidade", "estado"], how="outer")
    df_merged = df_merged.merge(df_csat, on=["data", "atendente", "supervisor", "coordenador", "operacao", "cidade", "estado"], how="outer")

    return df_merged

if __name__ == "__main__":
    # Exemplo de uso e validação
    try:
        df_raw = pd.read_csv("../data/call_center_data.csv")
        df_indicators = calculate_indicators(df_raw)
        print("Cálculo de indicadores concluído com sucesso!")
        print("Primeiras 5 linhas do DataFrame de indicadores:")
        print(df_indicators.head())

        # Validação básica
        # Verificar se não há valores nulos nos indicadores calculados (onde deveriam existir)
        print("\nVerificando valores nulos nos indicadores:")
        print(df_indicators[["Atendidas", "TMA", "CSAT"]].isnull().sum())

        # Verificar se os valores estão dentro de um range esperado (ex: CSAT entre 1 e 5)
        print("\nVerificando range do CSAT:")
        print(f"CSAT Mínimo: {df_indicators['CSAT'].min()}")
        print(f"CSAT Máximo: {df_indicators['CSAT'].max()}")

    except FileNotFoundError:
        print("Erro: Arquivo call_center_data.csv não encontrado. Certifique-se de que os dados fictícios foram gerados.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")



