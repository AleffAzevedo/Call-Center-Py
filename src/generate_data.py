
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_fictitious_data(num_rows=1000):
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 7, 28)

    dates = [start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days)) for _ in range(num_rows)]
    
    atendentes = [f'Atendente_{i}' for i in range(1, 21)]
    supervisores = [f'Supervisor_{i}' for i in range(1, 6)]
    coordenadores = [f'Coordenador_{i}' for i in range(1, 3)]
    operacoes = ['Vendas', 'Suporte Técnico', 'Cobrança', 'SAC']
    cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre', 'Curitiba']
    estados = ['SP', 'RJ', 'MG', 'RS', 'PR']
    
    data = {
        'data': dates,
        'atendente': np.random.choice(atendentes, num_rows),
        'supervisor': np.random.choice(supervisores, num_rows),
        'coordenador': np.random.choice(coordenadores, num_rows),
        'operacao': np.random.choice(operacoes, num_rows),
        'cidade': np.random.choice(cidades, num_rows),
        'estado': np.random.choice(estados, num_rows),
    }
    
    df = pd.DataFrame(data)

    # Gerar dados para os indicadores
    indicadores_data = []
    for index, row in df.iterrows():
        # Atendidas
        indicadores_data.append({
            'data': row['data'],
            'atendente': row['atendente'],
            'supervisor': row['supervisor'],
            'coordenador': row['coordenador'],
            'operacao': row['operacao'],
            'cidade': row['cidade'],
            'estado': row['estado'],
            'nome_indicador': 'Atendidas',
            'numerador': np.random.randint(5, 50), # Chamadas atendidas
            'denominador': 1 # Para Atendidas, o denominador é 1 (contagem simples)
        })
        
        # TMA (Tempo Médio de Atendimento) em segundos
        indicadores_data.append({
            'data': row['data'],
            'atendente': row['atendente'],
            'supervisor': row['supervisor'],
            'coordenador': row['coordenador'],
            'operacao': row['operacao'],
            'cidade': row['cidade'],
            'estado': row['estado'],
            'nome_indicador': 'TMA',
            'numerador': np.random.randint(60, 600), # Tempo total de atendimento em segundos
            'denominador': np.random.randint(5, 50) # Número de chamadas atendidas
        })
        
        # CSAT (Customer Satisfaction) - Escala de 1 a 5
        # Numerador: Soma das notas de satisfação
        # Denominador: Número de pesquisas respondidas
        num_pesquisas = np.random.randint(1, 10)
        soma_notas = np.random.randint(num_pesquisas, num_pesquisas * 5) # Garante que a média fique entre 1 e 5
        indicadores_data.append({
            'data': row['data'],
            'atendente': row['atendente'],
            'supervisor': row['supervisor'],
            'coordenador': row['coordenador'],
            'operacao': row['operacao'],
            'cidade': row['cidade'],
            'estado': row['estado'],
            'nome_indicador': 'CSAT',
            'numerador': soma_notas,
            'denominador': num_pesquisas
        })
        
    df_indicadores = pd.DataFrame(indicadores_data)
    return df_indicadores

if __name__ == '__main__':
    df_final = generate_fictitious_data(num_rows=5000) # Gerar 5000 linhas de dados
    df_final.to_csv('../app/data/call_center_data.csv', index=False)
    print('Dados fictícios gerados e salvos em bi_call_center/app/data/call_center_data.csv')


