import matplotlib.pyplot as plt

municipios = [
    "São Paulo","Guarulhos","Campinas","São Bernardo do Campo",
    "Santo André","Osasco","Sorocaba","Ribeirão Preto",
    "São José dos Campos","Mauá","Santos","Mogi das Cruzes",
    "Diadema","Jundiaí","Piracicaba","Bauru","São Vicente",
    "Franca","Itaquaquecetuba","Praia Grande","Limeira",
    "Suzano","Taubaté","Barueri","Indaiatuba",
    "Araraquara","Marília","Americana","Jacareí","Hortolândia"
]

populacao = [
    11451245,1291784,1139047,810729,748919,743432,723574,
    698642,697428,418261,418608,451505,393237,423006,
    423323,379297,329911,352536,369275,349935,291869,
    329216,310739,316473,255748,242228,237627,237240,
    240275,221428
]

plt.figure(figsize=(16,8))

plt.bar(
    municipios,
    populacao,
    color='steelblue',
    label='População dos Municípios'
)

plt.title(
    'População dos Municípios Paulistas Selecionados (Censo 2022)',
    fontsize=14
)

plt.xlabel('Municípios')
plt.ylabel('População (Habitantes)')

plt.xticks(rotation=90)

plt.grid(
    axis='y',
    linestyle='--',
    alpha=0.7
)

plt.legend()

plt.tight_layout()

plt.show()