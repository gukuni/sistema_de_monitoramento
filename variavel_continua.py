import pandas as pd

densidade = [
7527.8,4030.4,1429.0,1986.0,4267.0,11445.5,
1614.9,1078.5,637.5,6827.0,1494.3,635.0,
12800.0,980.0,307.0,567.6,2230.0,581.0,
4500.0,2340.0,502.0,1600.0,496.0,4820.0,
819.0,241.0,203.0,1770.0,518.0,3500.0
]

# Classes definidas manualmente
classes = [0, 2500, 5000, 7500, 10000, 13000]

freq = pd.cut(
    densidade,
    bins=classes,
    include_lowest=True
)

freq_abs = freq.value_counts().sort_index()

tabela = pd.DataFrame({
    "Classe": freq_abs.index.astype(str),
    "Freq. Absoluta": freq_abs.values
})

tabela["Freq. Relativa (%)"] = (
    tabela["Freq. Absoluta"] /
    tabela["Freq. Absoluta"].sum() * 100
).round(2)

tabela["Freq. Acumulada"] = (
    tabela["Freq. Absoluta"].cumsum()
)

tabela["Freq. Relativa Acumulada (%)"] = (
    tabela["Freq. Relativa (%)"].cumsum()
).round(2)

print(tabela)