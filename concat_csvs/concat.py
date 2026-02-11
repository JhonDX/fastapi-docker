import pandas as pd 
import os 
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]              
ENV_PATH = BASE_DIR / ".env_local"
load_dotenv(ENV_PATH, override=True)
arquivo_cupom = os.getenv("PATH_CUPOM")
arquivo_recompras = os.getenv("PATH_RECOMPRAS")
arquivo_vencimentos = os.getenv("PATH_VENCIMENTOS")

if not all([arquivo_cupom, arquivo_recompras, arquivo_vencimentos]):
    raise ValueError("Algum caminho não foi carregado do .env_local")

df_cupom = pd.read_csv(arquivo_cupom, encoding="utf-8", delimiter=';', low_memory=False)
df_recompras = pd.read_csv(arquivo_recompras, encoding="utf-8", delimiter=';', low_memory=False)
df_vencimentos = pd.read_csv(arquivo_vencimentos, encoding="utf-8", delimiter=';', low_memory=False)

colunas = [
    "Tipo Titulo",
    "Vencimento do Titulo",
    "Data Resgate",
    "PU",
    "Quantidade",
    "Valor",
]

df_cupom = df_cupom.reindex(columns=colunas)
df_recompras = df_recompras.reindex(columns=colunas)
df_vencimentos = df_vencimentos.reindex(columns=colunas)

df_cupom["Tipo_evento"] = "Cupom"
df_recompras["Tipo_evento"] = "Recompra"
df_vencimentos["Tipo_evento"] = "Vencimento"


df_geral = pd.concat([df_cupom, df_recompras, df_vencimentos], ignore_index=True)
caminho_pasta = os.getenv("PATH_DIR_CONCAT")
nome_arquivo = "tesouro_direto.csv"
caminho_completo = os.path.join(caminho_pasta, nome_arquivo)
df_geral.to_csv(caminho_completo, index= False)
print("Arquivo Gerado!")