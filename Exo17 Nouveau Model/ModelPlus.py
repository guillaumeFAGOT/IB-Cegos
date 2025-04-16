from faker import Faker
import csv
separator = "," 
# Créer une instance Faker avec la locale française
fake = Faker('fr_FR')

# Générer une liste de 10 noms complets français
# Définir le nom du fichier
file_name = "surveillants.csv"

# Afficher la liste
LigneFichier = ["Surveillant"]
data = []
for i in range(1, 15):
    data.append({
        #"ID Client": i,
        #"Nom": faker.last_name(),
        #"Prénom": faker.first_name(),
        #"Email": faker.email(),
        #"Téléphone": faker.phone_number(),
        #"Adresse": faker.street_address(),
        
        "Surveillant": fake.name(),
        
    })
    
# Écriture dans un fichier CSV
with open(file_name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=LigneFichier, delimiter=separator)
    writer.writeheader()  # Écrire les en-têtes
    writer.writerows(data)  # Écrire les lignes

print(f"Fichier généré : {file_name} .")
