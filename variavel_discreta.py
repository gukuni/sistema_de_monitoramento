
import pandas as pd


populacao = [
11451245,1291784,1139047,810729,748919,743432,723574,
698642,697428,418261,418608,451505,393237,423006,
423323,379297,329911,352536,369275,349935,291869,
329216,310739,316473,255748,242228,237627,237240,
240275,221428
]

faixas = [
0,300000,600000,900000,
1200000,1500000,12000000
]

freq = pd.cut(populacao, bins=faixas)

tabela = freq.value_counts().sort_index()

resultado = pd.DataFrame({
    'Classe': tabela.index.astype(str),
    'Freq. Absoluta': tabela.values
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
