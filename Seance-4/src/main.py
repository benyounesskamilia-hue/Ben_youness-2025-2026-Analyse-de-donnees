#coding:utf8

import numpy as np
import pandas as pd
import scipy
import scipy.stats
import matplotlib.pyplot as plt
from scipy.stats import norm, lognorm, uniform, chi2, pareto, poisson, randint, binom, zipf
import os

#https://docs.scipy.org/doc/scipy/reference/stats.html


dist_names = ['norm', 'beta', 'gamma', 'pareto', 't', 'lognorm', 'invgamma', 'invgauss',  'loggamma', 'alpha', 'chi', 'chi2', 'bradford', 'burr', 'burr12', 'cauchy', 'dweibull', 'erlang', 'expon', 'exponnorm', 'exponweib', 'exponpow', 'f', 'genpareto', 'gausshyper', 'gibrat', 'gompertz', 'gumbel_r', 'pareto', 'pearson3', 'powerlaw', 'triang', 'weibull_min', 'weibull_max', 'bernoulli', 'betabinom', 'betanbinom', 'binom', 'geom', 'hypergeom', 'logser', 'nbinom', 'poisson', 'poisson_binom', 'randint', 'zipf', 'zipfian']

# Question 1 & 2 : visualisation de distributions théoriques  et moyennes et écart-type de chacune de ces distributions 
# proposer les distributions discrètes : dirac, uniforme, binomiale, poisson, zipf
distri_discretes = ['dirac', 'uniforme', 'binomiale', 'poisson', 'zipf']
print ("distributions discretes porposées :", distri_discretes)

# définir les distributions discrètes dans une fonction de choix
def choix_distri_discretes(dist_name_discr):
    dist_name_discr = dist_name_discr.lower()
    if dist_name_discr == "dirac":
        x = np.arange(0, 10)
        p = np.zeros_like(x, dtype=float)
        p[3] = 1.0
        title = "Loi de Dirac (x=3)"
        moyenne = 3
        print ("moyenne :", moyenne)
        ecart_type = 0
        print ("ecart type :", ecart_type)
    elif dist_name_discr == "uniforme":
        x = np.arange(1, 7)
        p = randint.pmf(x, 1, 7)
        title = "Loi Uniforme Discrète [1, 6]"
        moyenne = randint.mean(1, 7)
        print ("moyenne :", moyenne)
        ecart_type = randint.std(1, 7, loc=0)
        print ("ecart type :", ecart_type)
    elif dist_name_discr == "binomiale":
        x = np.arange(0, 11)
        p = binom.pmf(x, 10, 0.5)
        title = "Loi Binomiale (n=10, p=0.5)"
        moyenne = binom.mean(10, 0.5, loc=0)
        print ("moyenne :", moyenne)
        ecart_type = binom.std(10, 0.5, loc=0)
        print ("ecart type :", ecart_type)
    elif dist_name_discr == "poisson":
        x = np.arange(0, 15)
        p = poisson.pmf(x, 3)
        title = "Loi de Poisson (λ=3)"
        moyenne = poisson.mean (3, loc=0)
        print ("moyenne :", moyenne)
        ecart_type = poisson.std (3, loc=0)
        print ("ecart type :", ecart_type)
    elif dist_name_discr == "zipf":
        x = np.arange(1, 20)
        p = zipf.pmf(x, 4)
        title = "Loi de Zipf (a=4)"
        moyenne = zipf.mean (a=4, loc=0)
        print ("moyenne :", moyenne)
        ecart_type = zipf.std (a=4, loc=0)
        print ("ecart type :", ecart_type)
    else:
        raise ValueError("Distribution inconnue")

    plt.figure()
    plt.bar(x, p)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("P(X = x)")

# Enregistrement dans le dossier figures_discretes
    dossier = "figures_discretes"
    os.makedirs(dossier, exist_ok=True)
    fichier = os.path.join(dossier, f"{title}.png")
    plt.savefig(fichier, bbox_inches='tight', dpi=300)
    print(f"Graphique enregistré dans : {fichier}")
    plt.show()

# choix de la distribution discrète théorique à afficher
choix_distri_discretes("Zipf")  # Exemple de choix de distribution


# proposer les distributions continues : poisson, normale, log-normale, uniforme, chi2, Pareto
distri_continues = ['poisson', 'normale', 'log-normale', 'uniforme', 'chi2', 'Pareto']
print ("distributions discretes porposées :", distri_continues)

# définir les distributions discrètes dans une fonction de choix
def choix_distri_continues(dist_name_cont):
    dist_name_cont = dist_name_cont.lower() #pour les erreurs de majuscules
    if dist_name_cont == "normale":
        x = np.linspace(-5, 5, 500)
        y = norm.pdf(x, 0, 1)    # 0 est loc=0 (moyenne), 1 est scale=1 (écart-type)
        title = "Loi Normale (μ=0, σ=1)"
        moyenne = norm.mean ()
        print ("moyenne :", moyenne)
        ecart_type = norm.std ()
        print ("ecart type :", ecart_type)

    elif dist_name_cont == "log-normale":
        x = np.linspace(0, 5, 500)
        y = lognorm.pdf(x, s=0.9)
        title = "Loi Log-Normale (s=0.9)" 
        moyenne = lognorm.mean(s=0.9)
        print ("moyenne :", moyenne)
        ecart_type = lognorm.std (s=0.9)
        print ("ecart type :", ecart_type)

    elif dist_name_cont == "uniforme":
        x = np.linspace(0, 1, 500)
        y = uniform.pdf(x, 0, 1)
        title = "Loi Uniforme Continue [0,1]"
        moyenne = uniform.mean()
        print ("moyenne :", moyenne)
        ecart_type = uniform.std ()
        print ("ecart type :", ecart_type)

    elif dist_name_cont == "chi2":
        x = np.linspace(0, 10, 500)
        y = chi2.pdf(x, df=3)
        title = "Loi du Chi² (df=3)"
        moyenne = chi2.mean(df=3)
        print ("moyenne :", moyenne)
        ecart_type = chi2.std (df=3)
        print ("ecart type :", ecart_type)

    elif dist_name_cont == "pareto":
        x = np.linspace(1, 5, 500)
        y = pareto.pdf(x, 3)
        title = "Loi de Pareto (b=3)"
        moyenne = pareto.mean(b=3)
        print ("moyenne :", moyenne)
        ecart_type = pareto.std (b=3)
        print ("ecart type :", ecart_type)

    elif dist_name_cont == "poisson":
        x = np.arange(0, 15)
        y = poisson.pmf(x, 3)
        title = "Loi de Poisson (λ=3)"
        moyenne = poisson.mean (3, loc=0)
        print ("moyenne :", moyenne)
        ecart_type = poisson.std (3, loc=0)
        print ("ecart type :", ecart_type)

    else:
        raise ValueError("Distribution inconnue")

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color='royalblue', linewidth=2)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, linestyle="--", alpha=0.5)

# Enregistrement dans le dossier figures_continues
    dossier = "figures_continues"
    os.makedirs(dossier, exist_ok=True)
    fichier = os.path.join(dossier, f"{title}.png")
    plt.savefig(fichier, bbox_inches='tight', dpi=300)
    print(f"Graphique enregistré dans : {fichier}")

# choix de la distribution discrète théorique à afficher
choix_distri_continues("poisson")  # Exemple de choix de distribution

