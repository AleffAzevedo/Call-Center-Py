import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

from calculate_indicators import calculate_indicators

# Configuração da página
st.set_page_config(
    page_title="BI Call Center",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("📞 Business Intelligence - Call Center")
st.markdown("---")

# Cache para carregar dados
@st.cache_data
def load_data():
    """Carrega e processa os dados do call center"""
    try:
        # Carregar dados brutos
        df_raw = pd.read_csv("call_center_data.csv")
        df_raw["data"] = pd.to_datetime(df_raw["data"])
        
        # Calcular indicadores
        df_indicators = calculate_indicators(df_raw)
        df_indicators["data"] = pd.to_datetime(df_indicators["data"])
        
        return df_raw, df_indicators
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return None, None

# Carregar dados
df_raw, df_indicators = load_data()

if df_raw is not None and df_indicators is not None:
    
    # Sidebar para filtros
    st.sidebar.header("🔍 Filtros")
    
    # Filtro de data
    min_date = df_indicators["data"].min().date()
    max_date = df_indicators["data"].max().date()
    
    date_range = st.sidebar.date_input(
        "Período",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Filtro de operação
    operacoes = ["Todas"] + list(df_indicators["operacao"].unique())
    operacao_selecionada = st.sidebar.selectbox("Operação", operacoes)
    
    # Filtro de estado
    estados = ["Todos"] + list(df_indicators["estado"].unique())
    estado_selecionado = st.sidebar.selectbox("Estado", estados)
    
    # Aplicar filtros
    df_filtered = df_indicators.copy()
    
    # Filtro de data
    if len(date_range) == 2:
        start_date, end_date = date_range
        df_filtered = df_filtered[
            (df_filtered["data"].dt.date >= start_date) & 
            (df_filtered["data"].dt.date <= end_date)
        ]
    
    # Filtro de operação
    if operacao_selecionada != "Todas":
        df_filtered = df_filtered[df_filtered["operacao"] == operacao_selecionada]
    
    # Filtro de estado
    if estado_selecionado != "Todos":
        df_filtered = df_filtered[df_filtered["estado"] == estado_selecionado]
    
    # Métricas principais
    st.header("📊 Métricas Principais")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_atendidas = df_filtered["Atendidas"].sum()
        st.metric("Total de Chamadas Atendidas", f"{total_atendidas:,.0f}")
    
    with col2:
        tma_medio = df_filtered["TMA"].mean()
        st.metric("TMA Médio (segundos)", f"{tma_medio:.1f}")
    
    with col3:
        csat_medio = df_filtered["CSAT"].mean()
        st.metric("CSAT Médio", f"{csat_medio:.2f}")
    
    with col4:
        total_atendentes = df_filtered["atendente"].nunique()
        st.metric("Total de Atendentes", total_atendentes)
    
    st.markdown("---")
    
    # Gráficos
    st.header("📈 Visualizações")
    
    # Linha 1 de gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Chamadas Atendidas por Dia")
        df_daily = df_filtered.groupby("data")["Atendidas"].sum().reset_index()
        fig_daily = px.line(df_daily, x="data", y="Atendidas", 
                           title="Evolução Diária de Chamadas Atendidas")
        fig_daily.update_layout(height=400)
        st.plotly_chart(fig_daily, use_container_width=True)
    
    with col2:
        st.subheader("TMA por Operação")
        df_tma_op = df_filtered.groupby("operacao")["TMA"].mean().reset_index()
        fig_tma = px.bar(df_tma_op, x="operacao", y="TMA",
                        title="Tempo Médio de Atendimento por Operação")
        fig_tma.update_layout(height=400)
        st.plotly_chart(fig_tma, use_container_width=True)
    
    # Linha 2 de gráficos
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("CSAT por Estado")
        df_csat_estado = df_filtered.groupby("estado")["CSAT"].mean().reset_index()
        fig_csat = px.bar(df_csat_estado, x="estado", y="CSAT",
                         title="Satisfação do Cliente por Estado")
        fig_csat.update_layout(height=400)
        st.plotly_chart(fig_csat, use_container_width=True)
    
    with col2:
        st.subheader("Distribuição de Chamadas por Operação")
        df_op_dist = df_filtered.groupby("operacao")["Atendidas"].sum().reset_index()
        fig_pie = px.pie(df_op_dist, values="Atendidas", names="operacao",
                        title="Distribuição de Chamadas por Operação")
        fig_pie.update_layout(height=400)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    st.markdown("---")
    
    # Tabela de dados
    st.header("📋 Dados Detalhados")
    
    # Top 10 atendentes
    st.subheader("Top 10 Atendentes por Chamadas Atendidas")
    top_atendentes = df_filtered.groupby("atendente").agg({
        "Atendidas": "sum",
        "TMA": "mean",
        "CSAT": "mean"
    }).round(2).sort_values("Atendidas", ascending=False).head(10)
    
    st.dataframe(top_atendentes, use_container_width=True)
    
    # Explicação do modelo numerador/denominador
    st.markdown("---")
    st.header("🧮 Modelo Numerador/Denominador")
    
    with st.expander("Como funciona o cálculo dos indicadores"):
        st.markdown("""
        ### Metodologia de Cálculo
        
        Este dashboard utiliza o modelo **numerador/denominador** para calcular os indicadores de forma flexível e escalável:
        
        **📞 Atendidas:**
        - Numerador: Número de chamadas atendidas
        - Denominador: 1 (contagem simples)
        - Cálculo: Soma dos numeradores
        
        **⏱️ TMA (Tempo Médio de Atendimento):**
        - Numerador: Tempo total de atendimento (segundos)
        - Denominador: Número de chamadas atendidas
        - Cálculo: Soma dos numeradores ÷ Soma dos denominadores
        
        **😊 CSAT (Customer Satisfaction):**
        - Numerador: Soma das notas de satisfação
        - Denominador: Número de pesquisas respondidas
        - Cálculo: Soma dos numeradores ÷ Soma dos denominadores
        
        ### Vantagens do Modelo:
        - ✅ Flexibilidade para adicionar novos indicadores
        - ✅ Facilidade de agregação em diferentes níveis
        - ✅ Consistência nos cálculos
        - ✅ Escalabilidade para grandes volumes de dados
        """)
    
else:
    st.error("Não foi possível carregar os dados. Verifique se o arquivo de dados existe.")
    st.info("Execute primeiro o script de geração de dados: `python src/generate_data.py`")


