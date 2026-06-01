import pandas as pd

densidade = [
7527.8,4030.4,1429.0,1986.0,4267.0,11445.5,
1614.9,1078.5,637.5,6827.0,1494.3,635.0,
12800.0,980.0,307.0,567.6,2230.0,581.0,
4500.0,2340.0,502.0,1600.0,496.0,4820.0,
819.0,241.0,203.0,1770.0,518.0,3500.0
]

serie = pd.Series(densidade)

print("MEDIDAS DE TENDÊNCIA CENTRAL")
print("Média:", serie.mean())
print("Mediana:", serie.median())
print("Moda:")
print(serie.mode())

print("\nMEDIDAS DE DISPERSÃO")
print("Máximo:", serie.max())
print("Mínimo:", serie.min())
print("Amplitude:", serie.max() - serie.min())
print("Variância:", serie.var())
print("Desvio Padrão:", serie.std())
print("Coeficiente de Variação (%):",
      (serie.std()/serie.mean())*100)

print("\nQUARTIS")
print(serie.quantile([0.25,0.50,0.75]))