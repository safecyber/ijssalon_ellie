from helper import onderstreep

uitvoer = onderstreep("aanbieding")
uitvoer.append("Aardbeienijs, emmertje van 5 liter: 5 euro.")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro.")

print()

for item in uitvoer:
    print(item)