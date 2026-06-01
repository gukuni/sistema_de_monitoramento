import pandas as pd
import numpy as np

populacao = [
11451245,1291784,1139047,810729,748919,743432,723574,
698642,697428,418261,418608,451505,393237,423006,
423323,379297,329911,352536,369275,349935,291869,
329216,310739,316473,255748,242228,237627,237240,
240275,221428
]

serie = pd.Series(populacao)

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