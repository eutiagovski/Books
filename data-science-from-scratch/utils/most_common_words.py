import sys

from collections import Counter

try:
    num_words = int(sys.argv[1])
except:
    print("usage: most_common_words.py num_words")

counter = Counter(word.lower()                      # palavras em minúscula
                  for line in sys.stdin             # para cada linha
                  for word in line.strip().split()  # divida nos espacos
                  if word)                          # se a palavra existir 

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")




