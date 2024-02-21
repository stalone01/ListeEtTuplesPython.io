# demander des noms de personnes
# boucle infinie, sort quand le est vide, ==> break
# seulement à la fin afficher tous les noms

# noms = []

# while True:
#     nom = input("Nom de la personne : ")
#     if nom == "":
#         break
#     noms.append(nom)

# print()

# print("Nom des personnes : ")
# noms.sort()
# for nom in noms:
#     print(' '+nom)

nom_chauffeur = ["patric","joseph","Marc","Jean","Pierre", "Marie", "maxime"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]

index_min = 0
distance_min = distance_chauffeur_km[0]
for i in range(len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i]
    if distance < distance_min :
        distance_min = distance
        index_min = i

print("Distance minimale :", distance_min,"km")
print("Index de la distance minimale :", index_min)
print("Nom du chauffeur:",nom_chauffeur[index_min])

noms_et_distances = [("Patric",1.5),("Paul",2.2),("Marc",0.4),("Jean",0.9),("Pierre",7.1),("Marie",1.1)]

nom_et_distance_min = noms_et_distances[0]
for nom_et_distance in noms_et_distances:
    if nom_et_distance[1] < nom_et_distance_min[1]:
        nom_et_distance_min = nom_et_distance

print("Distance minimale :", nom_et_distance_min[1], "nom du chauffeur :", nom_et_distance_min[0])