import matplotlib.pyplot as plt

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
    451505,
    418261,
    418608,
    393237,
    423006,
    423323
]

densidade = [
    7527.8,
    4030.4,
    1429.0,
    1986.0,
    4267.0,
    11445.5,
    1614.9,
    1078.5,
    637.5,
    635.0,
    6827.0,
    1494.3,
    12800.0,
    980.0,
    307.0
]

plt.figure(figsize=(10,6))

plt.scatter(
    populacao,
    densidade,
    color='darkred',
    s=80
)

plt.title('População x Densidade Demográfica dos Municípios')
plt.xlabel('População (habitantes)')
plt.ylabel('Densidade Demográfica (hab/km²)')

plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()