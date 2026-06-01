import pandas as pd

densidade = [
7527.8,4030.4,1429.0,1986.0,4267.0,11445.5,
1614.9,1078.5,637.5,6827.0,1494.3,635.0,
12800.0,980.0,307.0,567.6,2230.0,581.0,
4500.0,2340.0,502.0,1600.0,496.0,4820.0,
819.0,241.0,203.0,1770.0,518.0,3500.0
]

freq = pd.cut(
    densidade,
    bins=6
).value_counts().sort_index()

resultado = pd.DataFrame({
    'Classe': freq.index.astype(str),
    'Freq. Absoluta': freq.values
})

resultado['Freq. Relativa (%)'] = (
    resultado['Freq. Absoluta']
    / resultado['Freq. Absoluta'].sum()
    * 100
).round(2)

resultado['Freq. Acumulada'] = (
    resultado['Freq. Absoluta'].cumsum()
)

print(resultado)