import csv
from faker import Faker
from faker.providers import BaseProvider
import random



faker = Faker()


# Définir le nom du fichier
file_name = "commandant.csv"

# Définir les séparateurs ("," ou ";")
separator = ","  # Remplacez par "," si nécessaire

# Définir le nombre de lignes à générer
num_rows = 20

LigneFichier = ["Commandant"]
data = []
for i in range(1, num_rows + 1):
    data.append({
        #"ID Client": i,
        #"Nom": faker.last_name(),
        #"Prénom": faker.first_name(),
        #"Email": faker.email(),
        #"Téléphone": faker.phone_number(),
        #"Adresse": faker.street_address(),
        
        "Commandant": faker.last_name(),
        
    })
# Écriture dans un fichier CSV
with open(file_name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=LigneFichier, delimiter=separator)
    writer.writeheader()  # Écrire les en-têtes
    writer.writerows(data)  # Écrire les lignes

print(f"Fichier généré : {file_name} avec {num_rows} lignes.")
