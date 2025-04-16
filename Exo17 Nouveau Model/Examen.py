import csv
from faker import Faker
from faker.providers import BaseProvider
import random


class ProductProvider(BaseProvider):
    def Pilot_name(self):
        Pilot = [
            
"Corinne du Gaillard;1",
"Emmanuel Fernandes-Lopez	;	2	",
"Pauline Boulay	;3",
"Raymond-Philippe Bernard;4",
"Daniel Bertin-Martin;5",
"Thibaut Boulay;6",
"Jacqueline de Bruneau;7",
"Marguerite Michel;8",
"Augustin Gauthier-Allard;9",
"Marcel Didier;10",
"Sophie Parent;11",
"Théophile-Michel Renault;12",
"Juliette Renault;13",
"Eleonore Leroy Le Giraud;14"
        ]
        return self.random_element(Pilot)

    def Pays_name(self):
        pays = [
            "Math;1",
            "Hist-Géo;2",
            "Allemand;3",
            "Anglais;4",
            "Francais;5"
        ]
        return self.random_element(pays)

    def Piste_name(self):
        Piste = [
            "Loquidy;1",
            "Chavagne;2",
            "Notre Dame de toutes Aides;3",
            "La Perverie;4",
            "Lycée Clemenceau;5"
            "Lycée Saint Stanislas;6"
        ]
        return self.random_element(Piste)


    def  Plane_name(self):
        Plane = [
            "Examen Ier Trimestre;1",
            "Examen 2eme Trimestre;2",
            "Examen 3eme Trimestre;3",
        ]
        
        return self.random_element(Plane)
    
# Créer une instance de Faker
faker = Faker()
faker.add_provider(ProductProvider)
# Définir le nom du fichier
file_name = "Examen.csv"

# Définir les séparateurs ("," ou ";")
separator = ","  # Remplacez par "," si nécessaire

# Définir le nombre de lignes à générer
num_rows = 1000

# Colonnes du fichier
LigneFichier = ["Examens","Sujet", "Nom","Prénom", "Matiere","Lycée","Surveillant","Date"]

# Génération des données
data = []
for i in range(1, num_rows + 1):
    data.append({
        "Examens": i,
        "Sujet": faker.Plane_name(),
        "Nom": faker.last_name(),
        "Prénom": faker.first_name(),
        "Matiere": faker.Pays_name(),
        "Lycée": faker.Piste_name(),
        "Surveillant": faker.Pilot_name(),
        "Date": faker.date_time()
        
    })

# Écriture dans un fichier CSV
with open(file_name, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=LigneFichier, delimiter=separator)
    writer.writeheader()  # Écrire les en-têtes
    writer.writerows(data)  # Écrire les lignes

print(f"Fichier généré : {file_name} avec {num_rows} lignes.")

