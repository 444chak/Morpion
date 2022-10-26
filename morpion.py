"""
Morpion on shell
"""

from random import randint, choice



grille = [' ' for i in range(10)] #Initialisation de la grille. ' ' pour case vide.

def affGrille(): #Pour afficher une grille toute moche
  print('\033[2J\033[1;1H')
  print(f"""  |   | 
 {grille[1]}| {grille[2]} |{grille[3]}
---------
 {grille[4]}| {grille[5]} |{grille[6]}
---------
 {grille[7]}| {grille[8]} |{grille[9]}
  |   |""")

def placeGrille(t,p): #Place un symbole sur la grille. Renvoie faux si la case est non vide.
  if grille[p]==" ":
    if t=='X':
        grille[p]='\033[94m'+t+'\033[97m'
    elif t=='O':
        grille[p]='\033[92m'+t+'\033[97m'
    return True
  return False

def win(): #Vérifie que la grille actuelle a une victoire et renvoie le symbole victorieux le cas échéant.
  if grille[1]== grille[2] and grille[2]==grille[3] and grille[1]!=" ":
    return grille[1]
  if grille[4]== grille[5] and grille[4]==grille[6] and grille[4]!=" ":
    return grille[4]
  if grille[7]== grille[8] and grille[7]==grille[9] and grille[7]!=" ":
    return grille[7]
  if grille[1]== grille[4] and grille[1]==grille[7] and grille[1]!=" ":
    return grille[1]
  if grille[2]== grille[5] and grille[2]==grille[8] and grille[2]!=" ":
    return grille[2]
  if grille[3]== grille[6] and grille[3]==grille[9] and grille[3]!=" ":
    return grille[3]  
  if grille[1]== grille[5] and grille[1]==grille[9] and grille[1]!=" ":
    return grille[1]
  if grille[3]== grille[5] and grille[3]==grille[7] and grille[3]!=" ":
    return grille[3]
  if grille.count(' ')==1:
    return ' '
  return False

def legit(): #Renvoie les cases libres.
  res=[]
  for i in range(1,10):
    if grille[i]==' ':
      res.append(i)
  return res


def canWin2(symb, a, b,c):
  possibles = legit()
  if (grille[a] == symb and grille[b] == symb) or (grille[a] == symb and grille[c] == symb) or (grille[b] == symb and grille[c] == symb):
    if a in possibles: return a
    elif b in possibles: return b
    elif c in possibles: return c
def canWin(symb):
  cases = []
  cases.append(canWin2(symb, 1, 2, 3))
  cases.append(canWin2(symb, 4, 5, 6))
  cases.append(canWin2(symb, 7, 8, 9))
  cases.append(canWin2(symb, 1, 4, 7))
  cases.append(canWin2(symb, 2, 5, 8))
  cases.append(canWin2(symb, 3, 6, 9))
  cases.append(canWin2(symb, 1, 5, 9))
  cases.append(canWin2(symb, 3, 5, 7))
  for i in cases:
    if i != None: return i

#choisir le rejoignement des deux diagonales

def cpuJoue(symb): #L'ordinateur joue au hasard.
  cases = 0
  for i in grille:
    if i == '\033[94m'+"X"+'\033[97m': cases +=1
  wcases = 0
  for i in grille:
    if i == '\033[92m'+"O"+'\033[97m': wcases +=1
  possibles=legit()
  if canWin('\033[94m'+"X"+'\033[97m') != None: placeGrille(symb, canWin('\033[94m'+"X"+'\033[97m'))
  elif canWin('\033[92m'+"O"+'\033[97m') != None: placeGrille(symb, canWin('\033[92m'+"O"+'\033[97m'))
  elif wcases == 2 and cases == 1 and grille[1] == '\033[92m'+"O"+'\033[97m' and grille[9] == '\033[92m'+"O"+'\033[97m':
    placeGrille(symb,8)
  elif wcases == 2 and cases == 1 and grille[3] == '\033[92m'+"O"+'\033[97m' and grille[7] == '\033[92m'+"O"+'\033[97m':
    placeGrille(symb, 2)
  elif grille[5]== '\033[94m'+"X"+'\033[97m' and cases == 2:
    if grille[1] == '\033[94m'+"X"+'\033[97m' and grille[9]==' ': placeGrille(symb,9)
    elif grille[3] == '\033[94m'+"X"+'\033[97m' and grille[7]==' ': placeGrille(symb,7)
    elif grille[7] == '\033[94m'+"X"+'\033[97m' and grille[3]==' ': placeGrille(symb,3)
    elif grille[9] == '\033[94m'+"X"+'\033[97m' and grille[1]==' ': placeGrille(symb,1)
    elif grille[5]== '\033[94m'+"X"+'\033[97m':
      coins = []
      if 1 in possibles: coins.append(1)
      elif 3 in possibles: coins.append(3)
      elif 7 in possibles: coins.append(7)
      elif 9 in possibles: coins.append(9)
      placeGrille(symb, choice(coins))
  elif grille[5]==' ':
      placeGrille(symb,5)
  elif (grille[1]==' ' or grille[3]==' ' or grille[7]==' ' or grille[9]==' ') and grille[5]== '\033[94m'+"X"+'\033[97m':
    coins = []
    if 1 in possibles: coins.append(1)
    elif 3 in possibles: coins.append(3)
    elif 7 in possibles: coins.append(7)
    elif 9 in possibles: coins.append(9)
    placeGrille(symb, choice(coins))
  elif (grille[1]==' ' or grille[3]==' ' or grille[7]==' ' or grille[9]==' '):
    coins = []
    if 1 in possibles: coins.append(1)
    elif 3 in possibles: coins.append(3)
    elif 7 in possibles: coins.append(7)
    elif 9 in possibles: coins.append(9)
    placeGrille(symb, choice(coins))
  else:
    n = randint(0,len(possibles)-1)
    placeGrille(symb,possibles[n])



def joueurJoue(symb): #Jeu du joueur avec toutes les précautions.
  ligne=None
  while True:
    p=input("Où ? ")
    possibles=legit()
    try:
      p=int(p)
      if p<1 or p>9:
        print("Entre 1 et 9")
      else:
        if not placeGrille(symb,p):
          print("Emplacement déjà occupé.")
        else:
          print("ok")
          return
    except:
      print("Un entier entre 1 et 9.")


def play():
  winner = False
  current = randint(0,1)

  while not winner:
    affGrille()
    if current == 1:
      cpuJoue('X')
    else:
      joueurJoue('O')

    current = 1-current
    
    winner = win()
    
    affGrille()
    if winner not in ['\033[92m'+"O"+'\033[97m','\033[94m'+"X"+'\033[97m']:
      print('Egalité.')
    else:
      print(winner+' gagne.')


play()