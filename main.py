# main.py
from etl_pipeline import EltPiperline

if __name__ == "__main__":
    print("=== MODULO ETL (CENSO ESCOLAR) ===")

    pipeline = EltPiperline()
    pipeline.executar()
    pipeline.filtrar_e_salvar()

    print("=== FIM DO MODULO ===")
