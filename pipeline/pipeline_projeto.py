import pandas as pd
from sqlalchemy import create_engine, VARCHAR, Integer, Date, Float
import os 
from datetime import datetime

def extract():
    caminho_arquivo = os.getenv("PATH_TESOURO_DIRETO")
    if not caminho_arquivo:
        raise ValueError("Caminho do arquivo não reconhecido")
    df = pd.read_csv(caminho_arquivo, encoding= "utf-8", delimiter=',', low_memory=False)
    return df

def transform(df):
     #DATAFRAME TITULO
    df_titulo = df[["Tipo Titulo", "Vencimento do Titulo"]].reset_index(drop=True).drop_duplicates()
    colunas_titulo = {
        "Tipo Titulo" : "Tipo_titulo",
        "Vencimento do Titulo" : "Vencimento_titulo"
    }
    df_titulo.rename(columns=colunas_titulo, inplace = True)
    df_titulo["Vencimento_titulo"] = pd.to_datetime(df_titulo['Vencimento_titulo'], errors= "coerce", dayfirst=True)

    def validade_titulo(validade_titulo):
        today = datetime.now()
        if validade_titulo < today:
            return "Titulo vencido"
        else: 
            return "Titulo ainda válido"
        
    df_titulo['Titulo_id'] = df_titulo.index +1
    df_titulo['Validade_titulo'] = df_titulo['Vencimento_titulo'].apply(validade_titulo)
    df_titulo = df_titulo[["Titulo_id", "Tipo_titulo", "Vencimento_titulo", "Validade_titulo"]]

   #DATAFRAME MOVIMENTAÇÃO
    df_movimentacao = df[["Tipo Titulo", "Vencimento do Titulo", "Data Resgate", 
                          "Tipo_evento", "PU", "Quantidade", "Valor"]].reset_index(drop=True).drop_duplicates()
    colunas_movimentacao = {
        "Data Resgate" : "Data_resgate",
        "Vencimento do Titulo" : "Vencimento_titulo",
        "Tipo Titulo" : "Tipo_titulo"
    }

    df_movimentacao.rename(columns=colunas_movimentacao, inplace=True)

    for coluna_data in ["Data_resgate", "Vencimento_titulo"]:
        df_movimentacao[coluna_data] = pd.to_datetime(df_movimentacao[coluna_data], errors= "coerce", dayfirst= True)

    for coluna in ["PU", "Quantidade", "Valor"]:
        df_movimentacao[coluna] = df_movimentacao[coluna].astype(str).str.replace(",", ".", regex=False)
        df_movimentacao[coluna] = pd.to_numeric(df_movimentacao[coluna], errors="coerce")
        
    df_movimentacao["Mov_id"] = df_movimentacao.index +1 
    df_movimentacao = df_movimentacao.merge(
        df_titulo[["Titulo_id", "Tipo_titulo", "Vencimento_titulo"]],
        on=["Tipo_titulo", "Vencimento_titulo"],
        how="left"
    )
    df_movimentacao = df_movimentacao[["Mov_id", "Titulo_id", "Data_resgate", "Vencimento_titulo",
                                        "Tipo_evento", "PU", "Quantidade", "Valor"]]
    
    return df_titulo, df_movimentacao

def load(df_titulo, df_movimentacao):
    user = os.getenv("AIRFLOW_DB_USER")
    password = os.getenv("AIRFLOW_DB_PASSWORD")
    host = os.getenv("AIRFLOW_DB_HOST")
    port = os.getenv("AIRFLOW_DB_PORT")
    dbname = os.getenv("TESOURO_DB_NAME")


    if not all([user, password, host, port, dbname]):
        raise ValueError("Variaveis não indentificadas")

    conexao_banco = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    engine = create_engine(conexao_banco)
    tabela_titulo = "titulo"
    tabela_movimentacao = "movimentacao"

    df_titulo.to_sql(name = tabela_titulo, con = engine, index = False, if_exists = 'append', dtype = {
        "Titulo_id" : Integer,
        "Tipo_titulo" : VARCHAR(100),
        "Vencimento_titulo" : Date,
        "Validade_titulo" : VARCHAR(50)
    })

    df_movimentacao.to_sql(name = tabela_movimentacao, con = engine, index = False, if_exists = 'append', dtype = {
        "Mov_id" : Integer,
        "Titulo_id" : Integer,
        "Data_resgate" : Date,
        "Vencimento_titulo"	: Date,
        "Tipo_evento" :	VARCHAR(20),
        "PU" : Float,	
        "Quantidade" : Float,
        "Valor" : Float
    })
