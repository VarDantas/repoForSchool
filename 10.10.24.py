import random
import copy

def get_distance(star, centers):
    result = []
    for center_index in range(3):
        r = 0
        for i in range(2):
            r += (star[i]-centers[center_index][i])**2
        result.append(r**0.5)
    return result

def update_stars(stars, centers, star_to_cluster):
    for i in range(len(stars)):
        distance = get_distance(stars[i], centers)
        star_to_cluster[i] = distance.index(min(distance))
    return star_to_cluster

def update_centers(centers, stars, star_to_cluster):
    centers = centers[:]
    c = [[], [], []]
    for i, star in enumerate(stars):
        c[star_to_cluster[i]].append(star)
    new_centers = centers[:]
    for i in range(3):
        sum_x = 0
        sum_y = 0
        for star in c[i]:
            sum_x += star[0]
            sum_y += star[1]
        avg_center_x = sum_x/len(c[i])
        avg_center_y = sum_y/len(c[i])
        centers[i] = [avg_center_x, avg_center_y]
    return centers

with open("27B_18055.txt") as fn:
    lines = fn.readlines()[1:]
stars = []
for line in lines:
    line = line.replace(',', '.')
    new_star = list(map(float, line.split()))
    stars.append(new_star)

centers = []
for i in random.sample(range(len(stars)), 3):
    centers.append(stars[i].copy())
prev_centers = [0]*3
star_to_cluster = {i: -1 for i in range(len(stars))}

print(f"prev_centers = {prev_centers}")
print(f"centers = {centers}")
print("#"*80)

while centers != prev_centers:
    prev_centers = copy.deepcopy(centers)
    star_to_cluster = update_stars(stars, prev_centers, star_to_cluster)
    centers = update_centers(centers, stars, star_to_cluster)
    print(f"prev_centers = {prev_centers}")
    print(f"centers = {centers}")
    print("#"*80)

    x = 0
    y = 0
    for c in centers:
        x += c[0]
        y = c[1]
    print((100000*x/3, 100000*y/3))
