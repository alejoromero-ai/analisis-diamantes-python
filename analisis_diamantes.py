import pandas as pd 

df = pd.read_csv("diamonds.csv")

print (df.head())
print(df.shape)
print(df.info())

df["rango_precio"] = pd.cut(
    df["price"],
    bins=[0, 1000, 2500, 5000, 10000, float("inf")],
    labels=["Bajo", "Medio-bajo", "Medio", "Alto", "Muy alto"]
)

print(df[["price", "rango_precio"]].head(20))

print(df["rango_precio"].value_counts())

df.to_csv("diamonds_clasificado.csv", index=False)





































































































