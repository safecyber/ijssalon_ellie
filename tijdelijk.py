<<<<<<< HEAD
from helper import decoreer

def print_aanbieding():
  prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
  }
  aanbieding = prijzen["vanille"] * 0.8
  reclame_tekst = f"Vandaag in de aanbieding: vanille, 1 liter – slechts € {aanbieding}"
  reclame_tekst2 = reclame_tekst[:reclame_tekst.index('.') + 2]
  reclame_tekst3 = reclame_tekst2.upper()
  reclame_tekst4 = reclame_tekst3.split()
  reclame_tekst4 = ["Vandaag", "in", "de", "aanbieding:", "vanille-ijs,", "1", "liter", "–", "slechts", "€", "2.40"]
  for el in reclame_tekst4:
      if len(el) >= 5:
          print(el.upper())
      else:
          print(el.lower())
decoreer("Aanbieding")
print_aanbieding()
=======
prijzen = {
  "aardbei": 3,
  "vanille": 4,
  "chocolade": 5
}
aanbieding = prijzen["vanille"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[:reclame_tekst.index('.') + 2]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split()
reclame_tekst4 = ["Vandaag", "in", "de", "aanbieding:", "vanille-ijs,", "1", "liter", "–", "slechts", "€", "3.2"]
for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el.lower())


>>>>>>> db9a5e95278e2d76b7d2d97618aaa633fc99eb48





