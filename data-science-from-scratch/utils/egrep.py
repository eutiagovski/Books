# egrep.py
import sys, re


# sys.argv é a lista de argumentos de linha de comando
# sys.argv[0] é o nome do programa
# sys.argv[1] será o regex especificado na linha de comando
regex = sys.argv[1]

# para cada linha
for line in sys.stdin:
    # se corresponder ao regex
    if re.search(regex, line):
        sys.stdout.write(line)