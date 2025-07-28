# 📞 Business Intelligence - Call Center

Um projeto didático que demonstra como construir um sistema de Business Intelligence completo em Python, utilizando dados fictícios de call center e o modelo numerador/denominador para cálculo de indicadores.

## 🎯 Objetivo

Este projeto foi desenvolvido para demonstrar de forma prática e didática:

- Como construir um sistema de BI do zero em Python
- A simplicidade e flexibilidade do modelo numerador/denominador
- Como calcular múltiplos indicadores de forma consistente
- Como criar dashboards interativos com Streamlit e Plotly

## 📊 Indicadores Implementados

### 📞 Atendidas
- **Descrição**: Total de chamadas atendidas
- **Cálculo**: Soma dos numeradores (cada chamada = 1)
- **Denominador**: 1 (contagem simples)

### ⏱️ TMA (Tempo Médio de Atendimento)
- **Descrição**: Tempo médio gasto por chamada em segundos
- **Cálculo**: Soma dos tempos totais ÷ Soma das chamadas atendidas
- **Numerador**: Tempo total de atendimento (segundos)
- **Denominador**: Número de chamadas atendidas

### 😊 CSAT (Customer Satisfaction)
- **Descrição**: Satisfação média do cliente (escala 1-5)
- **Cálculo**: Soma das notas ÷ Número de pesquisas respondidas
- **Numerador**: Soma das notas de satisfação
- **Denominador**: Número de pesquisas respondidas

## 🏗️ Arquitetura do Projeto

```
Call-Center-Py/
├── src/
│   ├── generate_data.py              # Gerador de dados fictícios
│   └── calculate_indicators.py       # Motor de cálculo de indicadores
│   └── call_center_data.csv          # Base de dados fictícia
├── app/
│   └── dashboard.py                  # Dashboard interativo Streamlit
└── README.md                         # Documentação do projeto
```

## 🚀 Como Executar

### Pré-requisitos

```bash
pip install pandas numpy streamlit plotly
```

### Passo 1: Gerar Dados Fictícios

```bash
cd src
python generate_data.py
```

### Passo 2: Executar o Dashboard

```bash
cd app
streamlit run dashboard.py
```

O dashboard estará disponível em `https://call-center-py.streamlit.app/`

## 💡 Modelo Numerador/Denominador

### Conceito

O modelo numerador/denominador é uma abordagem elegante para calcular indicadores de forma consistente e escalável:

- **Numerador**: O valor que queremos somar/agregar
- **Denominador**: O valor pelo qual queremos dividir
- **Resultado**: Numerador ÷ Denominador

### Vantagens

✅ **Flexibilidade**: Fácil adição de novos indicadores
✅ **Consistência**: Todos os indicadores seguem a mesma lógica
✅ **Escalabilidade**: Funciona com grandes volumes de dados
✅ **Agregação**: Permite agregação em diferentes níveis (dia, mês, equipe, etc.)

### Exemplo Prático

Para calcular o TMA de uma equipe:

```python
# Dados individuais
atendente_1: numerador=300s, denominador=10 chamadas
atendente_2: numerador=450s, denominador=15 chamadas

# Agregação da equipe
tma_equipe = (300 + 450) / (10 + 15) = 750 / 25 = 30 segundos
```

## 📈 Funcionalidades do Dashboard

### Métricas Principais
- Total de chamadas atendidas
- TMA médio em segundos
- CSAT médio
- Total de atendentes ativos

### Visualizações Interativas
- Evolução diária de chamadas atendidas
- TMA por operação
- CSAT por estado
- Distribuição de chamadas por operação

### Filtros Disponíveis
- **Período**: Seleção de intervalo de datas
- **Operação**: Vendas, Suporte Técnico, Cobrança, SAC
- **Estado**: SP, RJ, MG, RS, PR

### Análises Detalhadas
- Ranking dos top 10 atendentes
- Tabela com métricas consolidadas
- Explicação didática do modelo numerador/denominador

## 🎓 Aprendizados

Este projeto demonstra conceitos importantes de:

- **Engenharia de Dados**: Geração e estruturação de dados
- **Business Intelligence**: Cálculo e apresentação de indicadores
- **Visualização de Dados**: Criação de dashboards interativos
- **Python**: Uso de pandas, numpy, streamlit e plotly
- **Arquitetura de Software**: Organização modular do código

## 🔧 Tecnologias Utilizadas

- **Python 3.11+**
- **Pandas**: Manipulação de dados
- **NumPy**: Operações numéricas
- **Streamlit**: Framework para dashboards web
- **Plotly**: Biblioteca de visualização interativa

## 📝 Estrutura dos Dados

### Campos da Base de Dados

| Campo | Tipo | Descrição |
|-------|------|-----------|
| data | datetime | Data do registro |
| atendente | string | Nome do atendente |
| supervisor | string | Nome do supervisor |
| coordenador | string | Nome do coordenador |
| operacao | string | Tipo de operação (Vendas, Suporte, etc.) |
| cidade | string | Cidade de origem |
| estado | string | Estado (SP, RJ, MG, RS, PR) |
| nome_indicador | string | Nome do indicador (Atendidas, TMA, CSAT) |
| numerador | float | Valor do numerador |
| denominador | float | Valor do denominador |

### Exemplo de Registros

```csv
data,atendente,supervisor,coordenador,operacao,cidade,estado,nome_indicador,numerador,denominador
2024-01-01,Atendente_1,Supervisor_1,Coordenador_1,Vendas,São Paulo,SP,Atendidas,25,1
2024-01-01,Atendente_1,Supervisor_1,Coordenador_1,Vendas,São Paulo,SP,TMA,750,25
2024-01-01,Atendente_1,Supervisor_1,Coordenador_1,Vendas,São Paulo,SP,CSAT,95,20
```

## 🤝 Contribuições

Este é um projeto didático aberto a contribuições! Algumas ideias para melhorias:

- Adicionar um sistema de Login/Logout
- Restrição de acesso de arcordo com o tipo usuário
- Adicionar novos indicadores (FCR, Abandono, etc.)
- Implementar filtros adicionais
- Criar visualizações mais avançadas
- Adicionar testes unitários
- Implementar cache para melhor performance

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor

Desenvolvido como projeto didático para demonstrar conceitos de Business Intelligence em Python.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!

