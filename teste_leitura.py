import pandas as pd

df = pd.read_csv("data/processed/censo_escolar_tratado.csv")

print("shape:", df.shape)
print("municipios unicos:", df["Municipio"].unique())
print("anos:", sorted(df["Ano"].unique()))
print(df.head(10))
