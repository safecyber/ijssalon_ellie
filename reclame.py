from aanbieding import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."

def inkomsten_totaal(inkomsten, btw=0):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    return min(mijn_lijst), max(mijn_lijst)

def gemiddelde(mijn_lijst):
    bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {bedrag} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    return meervoudig(invoer_lijst_2)


#test aanbieding_1 - aardbei
aanbieding_aardbei = aanbieding_1("aardbei", 4, 0.1) 
print(aanbieding_aardbei)
#test inkomsten_totaal
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
inkomsten = inkomsten_totaal(mijn_lijst, 0.09)
print(inkomsten)
#test laag_en_hoog
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
lh = laag_en_hoog(mijn_lijst)
print(lh)
#test gemiddelde
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
gem = gemiddelde(mijn_lijst)
print(gem)
#test meervoudig
mijn_lijst = [10,5,3,2,1,2,9]
uitkomst = meervoudig(mijn_lijst)
print(uitkomst) 
#test combinatie

korte_lijst = mijn_functie_2(uitkomst)
print(korte_lijst)




