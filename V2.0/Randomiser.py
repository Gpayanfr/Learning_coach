import random

# Ouverture du fichier .dcx en mode lecture
with open("fichier.dcx", "r") as file:
    # Lecture du contenu du fichier
    content = file.read()

# Recherche de tous les nombres décimaux dans le fichier
numbers = re.findall(r"\d+\.\d+", content)

# Boucle sur tous les nombres décimaux trouvés
for number in numbers:
    # Conversion du nombre en float
    float_number = float(number)
    # Génération d'un facteur aléatoire entre 0.5 et 2
    random_factor = random.uniform(0.5, 2)
    # Multiplication du nombre par le facteur aléatoire
    new_number = float_number * random_factor
    # Remplacement du nombre dans le contenu du fichier
    content = content.replace(number, str(new_number))

# Ouverture du fichier .dcx en mode écriture
with open("fichier.dcx", "w") as