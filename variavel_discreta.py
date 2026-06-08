
import pandas as pd

populacao = [
11451245,1291784,1139047,810729,748919,743432,723574,
698642,697428,418261,418608,451505,393237,423006,
423323,379297,329911,352536,369275,349935,291869,
329216,310739,316473,255748,242228,237627,237240,
240275,221428
]

serie = pd.Series(populacao)

freq_abs = serie.value_counts().sort_index()

tabela = pd.DataFrame({
    'População': freq_abs.index,
    'Freq. Absoluta': freq_abs.values
})

tabela['Freq. Relativa (%)'] = (
    tabela['Freq. Absoluta'] /
    tabela['Freq. Absoluta'].sum() * 100
)

tabela['Freq. Acumulada'] = (
    tabela['Freq. Absoluta'].cumsum()
)

tabela['Freq. Relativa Acumulada (%)'] = (
    tabela['Freq. Relativa (%)'].cumsum()
)

print(tabela)
