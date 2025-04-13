import csv
from faker import Faker
from faker.providers import BaseProvider
import random


class ProductProvider(BaseProvider):
    def Pilot_name(self):
        Pilot = [
            
            "Owens;1",
            "Prince;2",
            "Abbott;3",
            "Moore;4",
            "Doyle;5",
            "Mcclain;6",
            "Hale;7",
            "Johnston;8",
            "Hayden;9",
            "Hale;10",
            "York;11",
            "Hubbard;12",
            "Farrell;13",
            "Thompson;14",
            "Brown;15",
            "Davila;16",
            "Adams;17",
            "Hansen;18",
            "Sampson;19",
            "Mcdonald;20"
        ]
        return self.random_element(Pilot)

    def Pays_name(self):
        pays = [
            "France;1",
            "Britain;2",
            "Germany;3",
            "Belgium;4",
            "Italy;5"
        ]
        return self.random_element(pays)

    def Piste_name(self):
        Piste = [
            "North;1",
            "South;2",
            "West;3",
            "East;4",
        ]
        return self.random_element(Piste)


    def  Plane_name(self):
        Plane = [
            "Boeing;1",
            "Airbus;2",
        ]
        return self.random_element(Plane)
    
# Créer une instance de Faker
faker = Faker()
faker.add_provider(ProductProvider)
# Définir le nom du fichier
file_name = "Aeroport.csv"

# Définir les séparateurs ("," ou ";")
separator = ","  # Remplacez par "," si nécessaire

# Définir le nombre de lignes à générer
num_rows = 700

# Colonnes du fichier
LigneFichier = ["Vol","Avion", "Nom","Prénom", "Destination","Piste","Commmandant","Date"]

# Génération des données
data = []
for i in range(1, num_rows + 1):
    data.append({
        "Vol": i,
        "Avion": faker.Plane_name(),
        "Nom": faker.last_name(),
        "Prénom": faker.first_name(),
        "Destination": faker.Pays_name(),
        "Piste": faker.Piste_name(),
        "Commmandant": faker.Pilot_name(),
        "Date": faker.date_time()
        
    })

# Écriture dans un fichier CSV
with open(file_name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=LigneFichier, delimiter=separator)
    writer.writeheader()  # Écrire les en-têtes
    writer.writerows(data)  # Écrire les lignes

print(f"Fichier généré : {file_name} avec {num_rows} lignes.")

