#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import math

#Fonction pour ouvrir les fichiers
def ouvrirUnFichier(nom):
    with open(nom, "r", encoding="utf-8") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

#Fonction pour convertir les données en données logarithmiques
def conversionLog(liste):
    log = []
    for element in liste:
        log.append(math.log(element))
    return log

#Fonction pour trier par ordre décroissant les listes (îles et populations)
def ordreDecroissant(liste):
    liste.sort(reverse = True)
    return liste

#Fonction pour obtenir le classement des listes spécifiques aux populations
def ordrePopulation(pop, etat):
    ordrepop = []
    for element in range(0, len(pop)):
        if np.isnan(pop[element]) == False:
            ordrepop.append([float(pop[element]), etat[element]])
    ordrepop = ordreDecroissant(ordrepop)
    for element in range(0, len(ordrepop)):
        ordrepop[element] = [element + 1, ordrepop[element][1]]
    return ordrepop

#Fonction pour obtenir l'ordre défini entre deux classements (listes spécifiques aux populations)
def classementPays(ordre1, ordre2):
    classement = []
    if len(ordre1) <= len(ordre2):
        for element1 in range(0, len(ordre2) - 1):
            for element2 in range(0, len(ordre1) - 1):
                if ordre2[element1][1] == ordre1[element2][1]:
                    classement.append([ordre1[element2][0], ordre2[element1][0], ordre1[element2][1]])
    else:
        for element1 in range(0, len(ordre1) - 1):
            for element2 in range(0, len(ordre2) - 1):
                if ordre2[element2][1] == ordre1[element1][1]:
                    classement.append([ordre1[element1][0], ordre2[element2][0], ordre1[element][1]])
    return classement

#Partie sur les îles
iles = pd.DataFrame(ouvrirUnFichier("./data/island-index.csv"))
print(iles.head())

#Isoler la colonne des surfaces
surfaces = list(iles["Surface (km²)"])
surfaces = [float(x) for x in surfaces]


continents = [
    85545323, #Afrique / Asie / Europe
    37856841, #Amérique
    7768030, #Antarctique
    7605049, #Australie
]

surfaces.extend([float(v) for v in continents])

print("ajout ok")


#ordre décroissant des surfaces
surfaces_ordre = ordreDecroissant(surfaces)
print("Top 10 des plus grandes surfaces d'îles et continents:")
print(surfaces_ordre[0:10])

#Loi rang-taille
df = pd.DataFrame(surfaces_ordre, columns=["Surface (km²)"])
df["rang"] = range(1, len(df) + 1)

plt.figure(figsize=(7,5))
plt.loglog(df["rang"], df["Surface (km²)"], marker="o")
plt.title("Loi rang-taille des surfaces des îles et continents")
plt.xlabel("Rang")
plt.ylabel("Surface (km²)")
plt.grid(True, which="both", ls="--", alpha=0.4)
plt.tight_layout()
plt.savefig("loi_rang_taille_iles_continents.png")
plt.show()

print("image rang-taille ok")

#conversion logarithmique des surfaces
log_rang = conversionLog(df["rang"])
log_surface = conversionLog(df["Surface (km²)"])

plt.figure(figsize=(7,5))
plt.scatter(log_rang, log_surface)
plt.title("Conversion logarithmique des surfaces des îles et continents")
plt.xlabel("Log(Rang)")
plt.ylabel("Log(Surface (km²))")
plt.grid(True, which="both", ls="--", alpha=0.4)
plt.tight_layout()
plt.savefig("conversion_logarithmique_iles_continents.png")
plt.show()

print("image conversion logarithmique ok")

#Question 7
#Les rangs sont obtenus après un tri et ne sont donc pas des variables aléatoires indépendantes et identiquement distribuées. On ne peut donc pas effectuer de test mais on peut le faire sur les valeurs de la colonne du CSV directement. 

#Partie sur les populations des États du monde
#Source. Depuis 2007, tous les ans jusque 2025, M. Forriez a relevé l'intégralité du nombre d'habitants dans chaque États du monde proposé par un numéro hors-série du monde intitulé États du monde. Vous avez l'évolution de la population et de la densité par année.
monde = pd.DataFrame(ouvrirUnFichier("./data/Le-Monde-HS-Etats-du-monde-2007-2025.csv"))
print(monde.head())

#Isolement des colonnes
colonnes = ["État", "Pop 2007", "Pop 2025", "Densité 2007", "Densité 2025"]
donnees = monde[colonnes]

etats = list(donnees["État"])
pop2007 = list(donnees["Pop 2007"])
pop2025 = list(donnees["Pop 2025"])
densite2007 = list(donnees["Densité 2007"])
densite2025 = list(donnees["Densité 2025"])
print("isolation ok")

#ordre décroissant
ordrepop2007 = ordrePopulation(pop2007, etats)
ordrepop2025 = ordrePopulation(pop2025, etats)
ordredensite2007 = ordrePopulation(densite2007, etats)
ordredensite2025 = ordrePopulation(densite2025, etats)
print("extrait ordre pop 2007", ordrepop2007[0:10])
print("extrait ordre pop 2025", ordrepop2025[0:10])
print("extrait ordre densite 2007", ordredensite2007[0:10])
print("extrait ordre densite 2025", ordredensite2025[0:10])

#comparaison des listes
comparaison_liste = classementPays(ordrepop2007, ordredensite2025)
comparaison_liste.sort()
print("extrait comparaison liste", comparaison_liste[0:10])

#isolement colonnes
rangs_pop = []
rangs_densite = []
for element in comparaison_liste:
    rangs_pop.append(element[0])
    rangs_densite.append(element[1])

print("extrait rangs pop", rangs_pop[0:10])
print("extrait rangs densite", rangs_densite[0:10])

#calcul de corrélation et de concordance
from scipy.stats import spearmanr, kendalltau

correlation_spearman = spearmanr(rangs_pop, rangs_densite)
concordance_kendall = kendalltau(rangs_pop, rangs_densite)

print("Corrélation de Spearman :", correlation_spearman)
print("Concordance de Kendall :", concordance_kendall)

#BONUS partie île
required = {"Surface (km²)": surfaces_ordre, "Trait de côte (km)": list(iles["Trait de côte (km)"])}
surfaces = list(iles["Surface (km²)"])
surfaces = [float(x) for x in surfaces]
cote = list(iles["Trait de côte (km)"])
cote = [float(x) for x in cote]

rs = df.surfaces.rank(method="first", ascending=False)
rc = df.cote.rank(method="first", ascending=False)

pearson = df.surface.corr(df.cote)
spearman = rs.corr(rc, method="pearson")
kendall = rs.corr(rc, method="kendall")
ecart = (rs - rc).abs().sum()

print("Pearson :", pearson)
print("Spearman :", spearman)
print("Kendall :", kendall)
print("Écart de classement  :", ecart)
print("df", df.assign(rang_surface=rs, rang_cote=rc))


