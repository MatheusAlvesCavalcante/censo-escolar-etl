PROJETO: Análise do Censo Escolar - Fortaleza
EQUIPE: C

=== ARQUIVOS DE DADOS ===

1. DADOS ORIGINAIS (Pasta /data/raw)
- Fonte: INEP (Microdados do Censo Escolar)
- Arquivos: dados_2020.xlsx a dados_2025.xlsx
- Descrição: Planilhas brutas contendo estatísticas de matrículas por escola/município.
- Estrutura: Variável, com cabeçalhos inconsistentes entre anos (tratados via script).

2. DADOS TRATADOS (Pasta /data/processed)
- Arquivo: censo_escolar_tratado.csv
- Descrição: Dados consolidados e limpos focados no município de Fortaleza.
- Colunas:
  * Ano: Ano de referência do censo.
  * Municipio: Cidade (Filtrado para FORTALEZA).
  * Dependencia_Administrativa: Tipo de rede (Estadual, Municipal, etc).
  * [Categorias de Ensino]: Contagem de matrículas separadas por Parcial/Integral.
  * Nota: Os dados de 2025 foram mantidos no CSV mas marcados como "outliers" na análise.
