import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("filteringstars.csv")

star_names = df["Name"].tolist()
star_distances = df["Distance"].tolist()
star_masses = df["Mass"].tolist()
star_radiuses = df["Radius"].tolist()
star_gravities = df["Gravity"].tolist()

type = input('Type "M" for Mass, "R" for Radius, "D" for Distance, or "G" for Gravity: ')

fig = plt.figure(figsize = (20,20))

if (type.lower() == "m"):
    plt.barh(star_names,star_masses)
    plt.title("Names & Masses of the Stars")
    plt.ylabel("Masses")
elif (type.lower() == "r"):
    plt.barh(star_names,star_radiuses)
    plt.title("Names & Radiuses of the Stars")
    plt.ylabel("Radiuses")
elif (type.lower() == "d"):
    plt.barh(star_names,star_distances)
    plt.title("Names & Distances of the Stars")
    plt.ylabel("Distances")
elif (type.lower() == "g"):
    plt.barh(star_names,star_gravities)
    plt.title("Names & Gravities of the Stars")
    plt.ylabel("Gravities")

plt.xlabel("Names")
plt.show()

# All planets are within 100 lightyears
