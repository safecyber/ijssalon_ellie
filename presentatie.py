def presenteer(d,t):
    for key, value in d.items():
        print(f"{key} : {value} euro")
    print(f"="*40)
    print(f"totaal : {t} euro")
    print(f" ")

totaal = 50 
invoer = {'vis' : 10, 'vlees': 25, 'overig' : 15}
uitvoer = presenteer(invoer,totaal)

 
totaal = 5250
invoer = {'Aardbeien-ijs-totaal' : 1000, 'Vanille-ijs-totaal': 2000, 'Chocolade-ijs-totaal' : 15, 'Waterijsjes-totaal' : 750}
uitvoer = presenteer(invoer,totaal)
