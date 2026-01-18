# etl_pipeline.py
import pandas as pd
import os
from censo_processor import CensoProcessor
from config_etl import ARQUIVOS_ENTRADA, MUNICIPIO_ALVO, DIR_PROCESSED

class EltPiperline:
    def __init__(self):
        self.dados_consolidados = pd.DataFrame()

    def executar(self):
        dfs = []
        print("Iniciando pipeline...")

        for ano, arquivo in ARQUIVOS_ENTRADA.items():
            proc = CensoProcessor(ano, arquivo)
            proc.carregar_arquivos()
            proc.tratar_estrutura()
            proc.padronizar_dados()

            df_ano = proc.get_dados()
            if not df_ano.empty:
                dfs.append(df_ano)

        if dfs:
            self.dados_consolidados = pd.concat(dfs, ignore_index=True)
            print(f"[OK] Consolidado: {len(self.dados_consolidados)} linhas")
        else:
            print("[ERRO] Nenhum dado foi processado.")

    def filtrar_e_salvar(self):
        if self.dados_consolidados.empty:
            print("[ERRO] Nada para salvar.")
            return

        df_final = self.dados_consolidados.copy()

        # filtro CORRETO (mantém dataframe)
        df_final = df_final[df_final["Municipio"].str.strip() == MUNICIPIO_ALVO]


        df_final = df_final.sort_values(
            ["Ano", "Municipio", "Dependencia_Administrativa"],
            ascending=[True, True, True]
        )

        os.makedirs(DIR_PROCESSED, exist_ok=True)
        caminho_saida = os.path.join(DIR_PROCESSED, "censo_escolar_tratado.csv")

        df_final.to_csv(caminho_saida, index=False, encoding="utf-8-sig")

        print(f"[OK] CSV salvo em: {caminho_saida}")
        print(df_final.head())
