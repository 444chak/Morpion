"""
NAME : MORPION
AUTHOR : @444chak
LANG : FR
"""

# librairies
import pygame 
from pygame.locals import * 
from random import randint, choice


# window
pygame.init() 
window = pygame.display.set_mode((640,480)) 
pygame.display.set_caption("Morpion") # window title
icon = pygame.image.load("logo.png") # window icon
pygame.display.set_icon(icon)
background = pygame.image.load("bg.png") # background (avec grille)
opened = True


# fonts defined
font = pygame.font.Font("trebuc.ttf", 72) # titles
font2 = pygame.font.Font("trebuc.ttf", 25) # tours & exit & restart
font3 = pygame.font.Font("trebuc.ttf", 50) # result

# mode choice fonts
vs1 = font.render("1vs1", True, pygame.Color("#FFFFFF"))
vsIA = font.render("1vsIA", True, pygame.Color("#FFFFFF"))

# tour actuel fonts
tour = font2.render("Tour :", True, pygame.Color("#FFFFFF"))
tour1 = font2.render("JOUEUR 1 (X)", True, pygame.Color("#FF0000"))
tour2 = font2.render("JOUEUR 2 (O)", True, pygame.Color("#00FF00"))
tour3 = font2.render("IA (O)", True, pygame.Color("#00FF00"))

# exit & restart fonts
exit = font2.render("fermer", True, pygame.Color("#FFFFFF"))
restart = font2.render("restart", True, pygame.Color("#FFFFFF"))

# result fonts
win1 = font3.render("VICTOIRE - JOUEUR 1", True, pygame.Color("#FF0000"))
win2 = font3.render("VICTOIRE - JOUEUR 2", True, pygame.Color("#00FF00"))
win3 = font3.render("VICTOIRE - IA", True, pygame.Color("#00FF00"))
egalite = font3.render("ÉGALITÉ", True, pygame.Color("#FFFF00"))

# players symbols fonts
player = [
    ("X", font.render("X", True, pygame.Color("#FF0000"))),
    ("O", font.render("O", True, pygame.Color("#00FF00")))
]

# mode :
# -1 = not in game
# 0 = in game 1vs1
# 1 = in game 1vsIA
mode = -1

####################METHOD####################

class Morpion:
    def __init__(self, state, tour=-1):
        """
        Initialise le jeu
        ARG : 
            state : état de la partie (-1 : pas en jeu
                                        1 : 1vs1
                                        2 : 1vsIA
                                        3 : Victoire IA
                                        4 : Victoire Joueur)
            tour : 0 ou 1 selon le joueur
        """
        self.grille = [' ' for i in range(10)]
        self.state = state
        self.tour = tour
        self.plein = False
    def end(self, winner):
        """
        Défini le gagnant

        ARG : 
            winner : gagnant ("X" ou "O")
        """
        self.winner = winner

    def game(self, player, place):
        """
        Jouer sur une case
        
        ARG : 
            player : Symbole du joueur qui peut gagner ("X" ou "O")
            place : case à laquelle le joueur joue
        
        RETURN : 
            True : Lorsque le joueur a jouer
            False : Lorsque la case est occupée, le joueur n'a pas jouer
        """
        if play.win() == False:
            if self.grille[place] == " ":
                self.grille[place] = player[0]
                if play.tour == 1:
                    play.tour = 0
                elif play.tour == 0:
                    play.tour = 1
                return True
            return False

    def win(self): 
        """
        Check winner

        RETURN : Winner
        """
        if self.grille[1]== self.grille[2] and self.grille[2]==self.grille[3] and self.grille[1]!=" ":
            return self.grille[1]
        if self.grille[4]== self.grille[5] and self.grille[4]==self.grille[6] and self.grille[4]!=" ":
            return self.grille[4]
        if self.grille[7]== self.grille[8] and self.grille[7]==self.grille[9] and self.grille[7]!=" ":
            return self.grille[7]
        if self.grille[1]== self.grille[4] and self.grille[1]==self.grille[7] and self.grille[1]!=" ":
            return self.grille[1]
        if self.grille[2]== self.grille[5] and self.grille[2]==self.grille[8] and self.grille[2]!=" ":
            return self.grille[2]
        if self.grille[3]== self.grille[6] and self.grille[3]==self.grille[9] and self.grille[3]!=" ":
            return self.grille[3]  
        if self.grille[1]== self.grille[5] and self.grille[1]==self.grille[9] and self.grille[1]!=" ":
            return self.grille[1]
        if self.grille[3]== self.grille[5] and self.grille[3]==self.grille[7] and self.grille[3]!=" ":
            return self.grille[3]
        if self.grille.count(' ')==1:
            return ' '
        return False

    def legit(self):
        """
        RETURN : cases libres de la grille
        """
        self.res = []
        for i in range(1,10):
            if self.grille[i]==' ':
                self.res.append(i)
        return self.res

    def PreciseCanWin(self, symb, a, b,c):
        """
        Case à jouer pour gagner selon triplet

        ARG : 
            symb : Symbole du joueur qui peut gagner ("X" ou "O")
            a,b,c : Triplet des cases à vérifier
        
        RETURN : Case à jouer pour gagner
        """
        possibles = self.legit()
        if (self.grille[a] == symb and self.grille[b] == symb) or (self.grille[a] == symb and self.grille[c] == symb) or (self.grille[b] == symb and self.grille[c] == symb):
            if a in possibles: return a
            elif b in possibles: return b
            elif c in possibles: return c

    def canWin(self,symb):
        """
        Cases possibles pour gagner

        ARG : 
            symb : Symbole du joueur qui peut gagner ("X" ou "O")

        RETURN : Liste des cases possibles pour gagner
        """
        cases = []
        cases.append(self.PreciseCanWin(symb, 1, 2, 3))
        cases.append(self.PreciseCanWin(symb, 4, 5, 6))
        cases.append(self.PreciseCanWin(symb, 7, 8, 9))
        cases.append(self.PreciseCanWin(symb, 1, 4, 7))
        cases.append(self.PreciseCanWin(symb, 2, 5, 8))
        cases.append(self.PreciseCanWin(symb, 3, 6, 9))
        cases.append(self.PreciseCanWin(symb, 1, 5, 9))
        cases.append(self.PreciseCanWin(symb, 3, 5, 7))
        for i in cases:
            if i != None: return i

    def cpuJoue(self, symb): 
        """
        L'ordinateur joue

        ARG : 
            symb : Symbole du joueur qui peut gagner ("X" ou "O")
        """
        self.cases = 0
        for i in self.grille:
            if i == "X": self.cases +=1
        self.wcases = 0
        for i in self.grille:
            if i == "O": self.wcases +=1
        possibles=self.legit()
        if self.canWin("X") != None: 
            self.game(symb, self.canWin("X"))
        elif self.canWin("O") != None: self.game(symb, self.canWin("O"))
        elif self.wcases == 2 and self.cases == 1 and self.grille[1] == "O" and self.grille[9] == "O":
            self.game(symb, 8)
        elif self.wcases == 2 and self.cases == 1 and self.grille[3] == "O" and self.grille[7] == "O":
            self.game(symb, 2)
        elif self.grille[5]== "X" and self.cases == 2:
            if self.grille[1] == "X" and self.grille[9]==' ': self.game(symb, 9)
            elif self.grille[3] == "X" and self.grille[7]==' ': self.game(symb, 7)
            elif self.grille[7] == "X" and self.grille[3]==' ': self.game(symb, 3)
            elif self.grille[9] == "X" and self.grille[1]==' ': self.game(symb, 1)
            elif self.grille[5]== "X":
                self.coins = []
                if 1 in possibles: self.coins.append(1)
                elif 3 in possibles: self.coins.append(3)
                elif 7 in possibles: self.coins.append(7)
                elif 9 in possibles: self.coins.append(9)
                self.game(symb, choice(self.coins))
        elif self.grille[5]==' ':
            self.game(symb,5)
        elif (self.grille[1]==' ' or self.grille[3]==' ' or self.grille[7]==' ' or self.grille[9]==' ') and self.grille[5]== "X":
            self.coins = []
            if 1 in possibles: self.coins.append(1)
            elif 3 in possibles: self.coins.append(3)
            elif 7 in possibles: self.coins.append(7)
            elif 9 in possibles: self.coins.append(9)
            self.game(symb, choice(self.coins))
        elif (self.grille[1]==' ' or self.grille[3]==' ' or self.grille[7]==' ' or self.grille[9]==' '):
            self.coins = []
            if 1 in possibles: self.coins.append(1)
            elif 3 in possibles: self.coins.append(3)
            elif 7 in possibles: self.coins.append(7)
            elif 9 in possibles: self.coins.append(9)
            self.game(symb, choice(self.coins))
        else:
            n = randint(0,len(possibles)-1)
            self.game(symb,possibles[n])


# Coordonnées des cases sur la grille
place = [(220, 120), (300, 120),(380, 120),  (220, 200),(300, 200) , (380, 200),(220, 280) ,  (300, 280),(380, 280)]

####################JEU####################

play = Morpion(0)

while opened:
    
    window.blit(background, (0, 0))
    rect = pygame.Surface((640,480)) 
    rect.set_alpha(220)              
    rect.fill((0,0,0))         
    if mode == -1:  
        window.blit(rect, (0,0))   
        window.blit(vs1, (140, 190))
        window.blit(vsIA, (340, 190))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            opened = False 
        pos = pygame.mouse.get_pos()
        if mode == -1:
            if pos[0] >=150 and pos[0] <= 270 and pos[1] >=195 and pos[1] <= 260:
                vs1 = font.render("1vs1", True, pygame.Color("#FF0000"))
                if event.type == pygame.MOUSEBUTTONUP:
                    vs1.set_alpha(0)
                    vsIA.set_alpha(0)
                    rect.set_alpha(0)
                    mode = 0
                    play.state = 1
                    play.tour = randint(0, 1)
            elif pos[0] >=350 and pos[0] <= 510 and pos[1] >=195 and pos[1] <= 260:
                vsIA = font.render("1vsIA", True, pygame.Color("#FF0000"))
                if event.type == pygame.MOUSEBUTTONUP:
                    vs1.set_alpha(0)
                    vsIA.set_alpha(0)
                    rect.set_alpha(0)
                    mode = 1
                    play.state = 2
                    play.tour = randint(0, 1)

            else:
                vs1 = font.render("1vs1", True, pygame.Color("#FFFFFF"))
                vsIA = font.render("1vsIA", True, pygame.Color("#FFFFFF"))
        elif pos[0] >=190 and pos[0] <= 280 and pos[1] >=110 and pos[1] <= 190 and event.type == pygame.MOUSEBUTTONUP:
            if (play.tour == 1 and play.state == 2) ==False:
                play.game(player[play.tour], 1)
        elif pos[0] >=280 and pos[0] <= 370 and pos[1] >=110 and pos[1] <= 190 and event.type == pygame.MOUSEBUTTONUP:
            if (play.tour == 1 and play.state == 2) ==False: play.game(player[play.tour], 2)
        elif pos[0] >=370 and pos[0] <= 460 and pos[1] >=110 and pos[1] <= 190 and event.type == pygame.MOUSEBUTTONUP:
            if (play.tour == 1 and play.state == 2) ==False:
                play.game(player[play.tour], 3)

        elif pos[0] >=190 and pos[0] <= 280 and pos[1] >=190 and pos[1] <= 270 and event.type == pygame.MOUSEBUTTONUP:
            if (play.tour == 1 and play.state == 2) ==False:
                play.game(player[play.tour], 4)
        elif pos[0] >=280 and pos[0] <= 370 and pos[1] >=190 and pos[1] <= 270 and event.type == pygame.MOUSEBUTTONUP:
            if (play.tour == 1 and play.state == 2) ==False:
                play.game(player[play.tour], 5)
        elif pos[0] >=370 and pos[0] <= 460 and pos[1] >=190 and pos[1] <= 270 and event.type == pygame.MOUSEBUTTONUP:
            if (play.tour == 1 and play.state == 2) ==False:
                play.game(player[play.tour], 6)

        elif pos[0] >=190 and pos[0] <= 280 and pos[1] >=270 and pos[1] <= 350 and event.type == pygame.MOUSEBUTTONUP:
            if (play.tour == 1 and play.state == 2) ==False:
                play.game(player[play.tour], 7)
        elif pos[0] >=280 and pos[0] <= 370 and pos[1] >=270 and pos[1] <= 350 and event.type == pygame.MOUSEBUTTONUP:
            if (play.tour == 1 and play.state == 2) ==False:
                play.game(player[play.tour], 8)
        elif pos[0] >=370 and pos[0] <= 460 and pos[1] >=270 and pos[1] <= 350 and event.type == pygame.MOUSEBUTTONUP:
            if (play.tour == 1 and play.state == 2) ==False:
                play.game(player[play.tour], 9)
        if pos[0] >=280 and pos[0] <= 360 and pos[1] >=450 and pos[1] <= 480:
            exit = font2.render("fermer", True, pygame.Color("#FF0000"))
            if event.type == pygame.MOUSEBUTTONUP:
                opened = False 
        else:
            exit = font2.render("fermer", True, pygame.Color("#FFFFFF"))
        if pos[0] >=80 and pos[0] <= 150 and pos[1] >=450 and pos[1] <= 480:
            restart = font2.render("restart", True, pygame.Color("#FFFF00"))
            if event.type == pygame.MOUSEBUTTONUP and pos[0] >=80 and pos[0] <= 150 and pos[1] >=450 and pos[1] <= 480:
                mode = -1
                play.plein = False
                play.grille = [' ' for i in range(10)]
        else:
            restart = font2.render("restart", True, pygame.Color("#FFFFFF"))
       
    for x in range(1,10):
        if play.grille[x] == "X":
            window.blit(player[0][1], place[x-1])
        elif play.grille[x] == "O":
            window.blit(player[1][1], place[x-1])

    if play.grille[1] != " " and play.grille[2] != " " and play.grille[3] != " " and play.grille[4] != " " and play.grille[5] != " " and play.grille[6] != " " and play.grille[7] != " " and play.grille[8] != " " and play.grille[9] != " "  :
        play.plein = True

    if play.tour == 1 and play.state == 2 and play.plein == False and mode != -1:
        play.cpuJoue(player[play.tour])


    if play.tour == 0 and (play.state != 3 or play.state != 4) and mode != -1:
        window.blit(tour, (210, 50))
        window.blit(tour1, (280, 50))
    elif play.tour == 1 and play.state == 1 and mode != -1:
        window.blit(tour, (210, 50))
        window.blit(tour2, (280, 50))
    elif play.tour == 1 and play.state == 2 and mode != -1:
        window.blit(tour, (210, 50))
        window.blit(tour3, (280, 50))


    if (play.win() == "X" or play.win() == "O" or play.plein == True) and mode != -1:
        window.blit(rect, (0,0))   
        if play.win() == "X":
            window.blit(win1, (80, 200))
        elif play.win() == "O" and (play.state == 1 or play.state == 3):
            window.blit(win2, (80, 200))
            play.state = 3
        elif play.win() == "O" and (play.state == 2 or play.state == 4):
            window.blit(win3, (170, 200))
            play.state = 4
        elif play.state != 0: 
            window.blit(egalite, (230, 200))

    if play.state != 0 and mode != -1:
        window.blit(restart, (80, 450))
            
    window.blit(exit, (280, 450))

    pygame.time.Clock().tick(144)
    pygame.display.update()