# config_etl.py
import os

DIR_RAW = os.path.join("data", "raw")
DIR_PROCESSED = os.path.join("data", "processed")

ARQUIVOS_ENTRADA = {
    2020: "dados_2020.xlsx",
    2021: "dados_2021.xlsx",
    2022: "dados_2022.xlsx",
    2023: "dados_2023.xlsx",
    2024: "dados_2024.xlsx",
    2025: "dados_2025.xlsx",
}

MUNICIPIO_ALVO = "FORTALEZA"

# 14 colunas (a primeira é toda NaN no seu arquivo -> "Lixo")
COLUNAS_MAPEAMENTO = [
    "Lixo",
    "Descricao",
    "Creche_Parcial", "Creche_Integral",
    "Pre_Parcial", "Pre_Integral",
    "Fund_Iniciais_Parcial", "Fund_Iniciais_Integral",
    "Fund_Finais_Parcial", "Fund_Finais_Integral",
    "EJA_Parcial", "EJA_Integral",
    "Fundamental_Total",
    "Medio_Total",
]

COLUNAS_FINAIS = [
    "Ano",
    "Municipio",
    "Dependencia_Administrativa",
    "Creche_Parcial", "Creche_Integral",
    "Pre_Parcial", "Pre_Integral",
    "Fund_Iniciais_Parcial", "Fund_Iniciais_Integral",
    "Fund_Finais_Parcial", "Fund_Finais_Integral",
    "EJA_Parcial", "EJA_Integral",
    "Fundamental_Total",
    "Medio_Total",
]
