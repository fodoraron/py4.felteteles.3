'''
3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
'''

from random import randrange

randomszám = randrange(1,5)
print('kérek számot')
bemenet = int(input())
if bemenet == randomszám:
  print('egyezés')
elif bemenet > randomszám:
  print('nagyobb')
else:
  print('kissebb')