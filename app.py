import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración visual profesional
st.set_page_config(page_title="FinanCore-AI Dashboard", layout="wide")

st.title("📈 FinanCore-AI: Inteligencia Financiera")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Entrada de Datos")
    ingresos = st.number_input("Ingresos mensuales ($)", min_value=0, value=5000)
    gastos = st.number_input("Gastos operativos ($)", min_value=0, value=3000)

with col2:
    st.subheader("Análisis en Tiempo Real")
    beneficio = ingresos - gastos
    st.metric(label="Beneficio Neto", value=f"${beneficio:,.2f}")
    
    # Gráfico interactivo
    df = pd.DataFrame({'Categoría': ['Ingresos', 'Gastos'], 'Valor': [ingresos, gastos]})
    fig = px.pie(df, values='Valor', names='Categoría', 
                 color_discrete_map={'Ingresos':'#00CC96', 'Gastos':'#EF553B'})
    st.plotly_chart(fig, use_container_width=True)

st.success("Análisis completado con éxito.")
