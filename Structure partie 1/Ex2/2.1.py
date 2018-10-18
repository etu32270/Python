# Combinaison de deux listes en une seule
# Listes fournies au départ :
liste1 = [31,28,31,30,31,30,31,31,30,31,30,31]
liste2 = ['Janvier','Février','Mars','Avril','Mai','Juin',
'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
# Nouvelle liste à construire (vide au départ) :
liste3 = []
# Boucle de traitement :
i = 0
while i < len(liste1):
    liste3.append(liste2[i])
    liste3.append(liste1[i])
    i = i + 1
# Affichage :
print(liste3)