import random
import math
file = open('27_B_17834.txt')
star_coords = [list(map(float, line.strip().replace(',', '.').split())) for line in file if not('X') in line]

cluster1 = random.choice(star_coords)
cluster2 = random.choice(star_coords)

def EDistance(coord1, coord2):
    return math.sqrt((coord1[0]-coord2[0])**2 + (coord1[1]-coord2[1])**2)

for star in star_coords:
    d1 = EDistance(star, cluster1)
    d2 = EDistance(star, cluster2)
    print(f"Координаты: {star}, d до 1 кластера: {d1}, d до 2 кластера: {d2}")

maxd = 0
for i in range(len(star_coords)):
    for j in range(i+1, len(star_coords)):
        d = EDistance(star_coords[i], star_coords[j])
        if d > maxd:
            maxd = d
            cluster1 = star_coords[i]
            cluster2 = star_coords[j]

for star in star_coords:
    d1 = EDistance(star, cluster1)
    d2 = EDistance(star, cluster2)
    if d1 < d2:
        closest_cluster = 1
    else:
        closest_cluster = 2
    print(f"Координаты: {star}, ближайщий кластер: {closest_cluster}")
