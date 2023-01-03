import itertools

all_combinations = list(itertools.combinations(range(1, 50), 6))

fichier = open("data.txt", "w")

for i in range(0, len(all_combinations)-1):
    text = ', '.join(map(str, all_combinations[i]))
    fichier.write(text+'\n')

fichier.close()
print("Fichier écrit !")