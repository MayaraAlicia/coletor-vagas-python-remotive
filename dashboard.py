import streamlit as st
import pandas as pd
import sqlite3

con = sqlite3.connect('vagas.db')
df = pd.read_sql_query("SELECT * FROM VAGAS", con)

st.set_page_config(page_title="Central de Vagas", page_icon="💼", layout="wide")

st.markdown("""
    <style>
    .main {background-color: #104E8B;}
    .stButton>button {background-color: #EA1D2C; color: white;
    </style>
    """, unsafe_allow_html=True)

st.markdown("**Sistema de vagas de emprego para TI**")
st.title("💼 Central de Vagas de Emprego")

st.write(f"Total de vagas no banco de dados: {len(df)}")

senior = df['TITULO'].str.contains('Sênior|Senior|Sr|Sr.|Lead|Principal|Staff|Head', case = False, regex=True )
junior = df['TITULO'].str.contains('Junior|Júnior|Jr.|Jr|Entry Level|Intern|Trainee', case = False, regex=True )
outros = len(df) - senior.sum() - junior.sum()

st.markdown("### Quantidade de vagas por nível:")
st.write(f"Vagas para Nível Sênior: {senior.sum()}")
st.write(f"Vagas para Nível Júnior: {junior.sum()}")
st.write(f"Vagas para Outros Níveis: {outros}")

dados_grafico = {
    "Nível": ["Sênior", "Júnior", "Outros"],
    "Quantidade": [senior.sum(), junior.sum(), outros]
}

df_grafico = pd.DataFrame(dados_grafico)

st.bar_chart(df_grafico, x="Nível", y="Quantidade", use_container_width=True)
st.markdown("### Análise de Nível das Vagas")

st.data_editor(df, column_config={
    "TITULO": st.column_config.TextColumn("Cargo", help="Título da vaga de emprego"),
    "EMPRESA": st.column_config.TextColumn("Empresa", help="Nome da empresa que está oferecendo a vaga"),
    "CIDADE": st.column_config.TextColumn("Localização", help="Localização do candidato"),
    "DATA_COLETA": st.column_config.TextColumn("Data de Coleta", help="Data em que a vaga foi coletada"),})

con.close()
