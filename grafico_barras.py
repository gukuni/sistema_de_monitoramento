import matplotlib.pyplot as plt

municipios = [
    "São Paulo",
    "Guarulhos",
    "Campinas",
    "São Bernardo",
    "Santo André",
    "Osasco",
    "Sorocaba",
    "Ribeirão Preto",
    "São José dos Campos",
    "Mogi das Cruzes"
]

populacao = [
    11451245,
    1291784,
    1139047,
    810729,
    748919,
    743432,
    723574,
    698642,
    697428,
    451505
]

plt.figure(figsize=(12,6))

plt.bar(municipios, populacao, color='steelblue')

plt.title('População dos Municípios Paulistas - Censo 2022')
plt.xlabel('Municípios')
plt.ylabel('População (habitantes)')

plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()