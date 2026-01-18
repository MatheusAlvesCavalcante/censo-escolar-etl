# censo_processor.py
import pandas as pd
import os
from config_etl import COLUNAS_MAPEAMENTO, COLUNAS_FINAIS, DIR_RAW

class CensoProcessor:
    def __init__(self, ano, nome_arquivo):
        self.ano = ano
        self.caminho = os.path.join(DIR_RAW, nome_arquivo)
        self.df = pd.DataFrame()

    def carregar_arquivos(self):
        try:
            df = pd.read_excel(self.caminho, header=None)

            # remove linhas totalmente vazias
            df = df.dropna(how="all")

            # NÃO remover colunas totalmente vazias (no seu arquivo a col 0 é toda NaN)
            # df = df.dropna(axis=1, how="all")  # <- NÃO USE

            # garante 14 colunas
            df = df.iloc[:, :len(COLUNAS_MAPEAMENTO)]

            # (opcional) se por algum motivo vier com menos colunas, completa com NaN
            while df.shape[1] < len(COLUNAS_MAPEAMENTO):
                df[df.shape[1]] = pd.NA

            df.columns = COLUNAS_MAPEAMENTO
            self.df = df

            print(f"[OK] {self.ano}: carregou {os.path.basename(self.caminho)} - shape {self.df.shape}")

        except Exception as e:
            print(f"[ERRO] {self.ano}: falha ao carregar {self.caminho}: {e}")
            self.df = pd.DataFrame()

    def tratar_estrutura(self):
        if self.df.empty:
            return

        # Cabeçalho é a linha onde NÃO tem número em 'Creche_Parcial'
        self.df["Eh_Cabecalho"] = self.df["Creche_Parcial"].isna()

        # Municipio/UF vem nas linhas de cabeçalho (na coluna 'Descricao')
        self.df["Municipio"] = self.df["Descricao"].where(self.df["Eh_Cabecalho"]).ffill()

        # Dependência administrativa vem nas linhas de dados (também na 'Descricao')
        self.df["Dependencia_Administrativa"] = self.df["Descricao"].where(~self.df["Eh_Cabecalho"])

        # remove linhas de cabeçalho e lixo
        self.df = self.df[~self.df["Eh_Cabecalho"]].copy()
        self.df = self.df.dropna(subset=["Dependencia_Administrativa"])

    def padronizar_dados(self):
        if self.df.empty:
            return

        self.df["Ano"] = self.ano

        self.df["Municipio"] = (
            self.df["Municipio"].astype(str).str.upper().str.strip()
        )
        self.df["Dependencia_Administrativa"] = (
            self.df["Dependencia_Administrativa"].astype(str).str.upper().str.strip()
        )

        # converte todas as colunas numéricas
        cols_num = [c for c in COLUNAS_MAPEAMENTO if c not in ["Lixo", "Descricao"]]
        cols_num = [c for c in cols_num if c not in ["Municipio", "Dependencia_Administrativa"]]

        for col in cols_num:
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(self.df[col], errors="coerce").fillna(0)

        # deixa só no formato final
        self.df = self.df[COLUNAS_FINAIS]

    def get_dados(self):
        return self.df
