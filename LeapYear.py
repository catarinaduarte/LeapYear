

import sys

if len(sys.argv) != 2:
    print(f"Utilização: {sys.argv[0]} ANO")
    sys.exit(2)

ano = int(sys.argv[1])
if ano < 0:
    print("Ano inválido", ano)
    sys.exit(2)

if ano % 400 == 0 or (ano % 100 != 0 and ano % 4 == 0):
    print("Ano bissexto")
else:
    print("Ano não bissexto")


