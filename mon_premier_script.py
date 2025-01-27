"""message = "C'est mon premier script !!!"
print(message)"""

#----------Type de variable------------------
"""je_change_de_type = 1
print(type(je_change_de_type))
je_change_de_type = "coucou"
print(type(je_change_de_type))"""

#-------test code boucle for-----------------

"""prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
more_than_seven = 0
for prenom in prenoms:
    if len(prenom) > 7:
        more_than_seven += 1
        print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
    else:
        print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(more_than_seven))"""

#--------------Test Fonction-------------------------
"""def saluer(nom: str) -> str:
    return "Bonjour " + nom

print(saluer("Alice"))  # Affiche : Bonjour Alice"""

#-------Count name----------------
"""
Count names with more than seven letters
"""
"""def names(prenoms):
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
        else:
            print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
    return more_than_seven

prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(names(prenoms=prenoms)))"""

#-------- Test Unitaire -----------------------
'''import unittest

#Count names with more than seven letters

def count_long_names(prenoms):
    long_names_count = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            long_names_count += 1
            print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
        else:
            print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
    return long_names_count

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        long_names_count = count_long_names(prenoms=prenoms)
        self.assertEqual(long_names_count, 4)

if __name__ == '__main__':
    unittest.main()
'''

#------------------------Contrôle Continue---------------------------
#package
import unittest

# Fonction pour compter le nombre de prénom avec plus de sept lettres
def count_long_names(prenoms: list) -> int:
    number_letter = 7 # Nombre de lettre
    long_names_count = 0  # Compteur des prénoms ayant plus de sept lettres
    for prenom in prenoms:
        if len(prenom) > number_letter:
            long_names_count += 1  # On ajoute +1 quand le prénom à plus de sept lettres
            print(f"{prenom} est un prénom avec un nombre de lettres supérieur à {number_letter}")
        else:
            print(f"{prenom} est un prénom avec un nombre de lettres inférieur ou égal à {number_letter}")
    print("")
    print(f"Nombre de prénoms dont le nombre de lettres est supérieur à 7 : {long_names_count}")
    return long_names_count # On retourne le nombre de prénoms ayant plus de sept lettres

# Fonction pour le test unitaire
class TestNamesMethod(unittest.TestCase):
     def test_count_long_names(self): # Test pour valider notre fonction
        good_result = 4 # Résultat attendu de la fonction
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        long_names_count = count_long_names(prenoms=prenoms) # import de la fonction "count_long_names"
        self.assertEqual(long_names_count, good_result)

if __name__ == '__main__':
    unittest.main()

