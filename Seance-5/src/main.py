#coding:utf8

import pandas as pd
import math
import scipy
import scipy.stats

#C'est la partie la plus importante dans l'analyse de données. D'une part, elle n'est pas simple à comprendre tant mathématiquement que pratiquement. D'autre, elle constitue une application des probabilités. L'idée consiste à comparer une distribution de probabilité (théorique) avec des observations concrètes. De fait, il faut bien connaître les distributions vues dans la séance précédente afin de bien pratiquer cette comparaison. Les probabilités permettent de définir une probabilité critique à partir de laquelle les résultats ne sont pas conformes à la théorie probabiliste.
#Il n'est pas facile de proposer des analyses de données uniquement dans un cadre univarié. Vous utiliserez la statistique inférentielle principalement dans le cadre d'analyses multivariées. La statistique univariée est une statistique descriptive. Bien que les tests y soient possibles, comprendre leur intérêt et leur puissance d'analyse dans un tel cadre peut être déroutant.
#Peu importe dans quelle théorie vous êtes, l'idée de la statistique inférentielle est de vérifier si ce que vous avez trouvé par une méthode de calcul est intelligent ou stupide. Est-ce que l'on peut valider le résultat obtenu ou est-ce que l'incertitude qu'il présente ne permet pas de conclure ? Peu importe également l'outil, à chaque mesure statistique, on vous proposera un test pour vous aider à prendre une décision sur vos résultats. Il faut juste être capable de le lire.

#Par convention, on place les fonctions locales au début du code après les bibliothèques.
def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

#Théorie de l'échantillonnage (intervalles de fluctuation)
#L'échantillonnage se base sur la répétitivité.
print("Résultat sur le calcul d'un intervalle de fluctuation")

donnees = pd.DataFrame(ouvrirUnFichier("./data/Echantillonnage-100-Echantillons.csv"))

# =========================
# THÉORIE DE L'ÉCHANTILLONNAGE
# =========================

# Calcul des moyennes par modalité
moyennes = donnees.mean()
print("\nMoyennes des 100 échantillons :")
print(moyennes)

# Arrondi à 0 décimale (comme demandé)
moyennes_arrondies = moyennes.round(0)

# Somme des moyennes
effectif_total = moyennes_arrondies.sum()

# Fréquences issues de l'échantillonnage
frequences_echantillon = moyennes_arrondies / effectif_total
print("\nFréquences issues des échantillons :")
print(frequences_echantillon)

# Fréquences de la population mère (données de l'énoncé)
population = {
    "Pour": 852,
    "Contre": 911,
    "Sans opinion": 422
}

population = pd.Series(population)
frequences_population = population / population.sum()

print("\nFréquences de la population mère :")
print(frequences_population)

# Calcul des intervalles de fluctuation à 95 %
z = 1.96
n = effectif_total

print("\nIntervalles de fluctuation à 95 % :")

for modalite in frequences_echantillon.index:
    f = frequences_echantillon[modalite]
    marge = z * math.sqrt((f * (1 - f)) / n)
    borne_inf = f - marge
    borne_sup = f + marge

    print(modalite, ":", round(borne_inf, 3), ";", round(borne_sup, 3))


#Théorie de l'estimation (intervalles de confiance)
#L'estimation se base sur l'effectif.
print("Résultat sur le calcul d'un intervalle de confiance")

# =========================
# THÉORIE DE L'ESTIMATION
# =========================

# On choisit un seul échantillon (le premier)
echantillon = donnees.iloc[0]

print("\nÉchantillon étudié :")
print(echantillon)

# Effectif de l'échantillon
n_ech = echantillon.sum()

print("\nIntervalle de confiance à 95 % :")

for modalite in echantillon.index:
    f = echantillon[modalite] / n_ech
    marge = z * math.sqrt((f * (1 - f)) / n_ech)
    borne_inf = f - marge
    borne_sup = f + marge

    print(modalite, ":", round(borne_inf, 3), ";", round(borne_sup, 3))

#Théorie de la décision (tests d'hypothèse)
#La décision se base sur la notion de risques alpha et bêta.
#Comme à la séance précédente, l'ensemble des tests se trouve au lien : https://docs.scipy.org/doc/scipy/reference/stats.html
print("Théorie de la décision")
