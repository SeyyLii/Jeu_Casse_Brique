from Paddle import Paddle #import de la classe Paddle
from Ball import Ball
from Brick import Brick
import random

playingGame = False # détermine si le joueur peut jouer.
bricks = [] # création de la liste
score = 0 # création d'un score qui s'affichera en haut à droite

def mousePressed(): # Quand l'utilisateur clique, il pourra jouer
    global playingGame
    playingGame = True

def addBrick(x, y, hits): # Permet de créer des rangées de briques rapidement
    brick = Brick(x, y, hits) # Paramètres : Position sur l'axe des ordonnées et abscisses et la couleur de la brique
    bricks.append(brick) # ajoute cette nouvelle brique à la liste

def level(n): # Selection des niveaux
    global paddle, ball # on déclare la variable paddle et ball comme globale
    paddle = Paddle() # on crée l'objet paddle
    ball = Ball() # on crée l'objet ball

    if n == 1: # niveau 1
        # appel de la fonction addBrick pour ajouter les briques
        for x in range(5, width - 80, 80):
            addBrick(x + 37.5, 50, 1)
            addBrick(x + 37.5, 70, random.randint(1,2))
            addBrick(x + 37.5, 90, 1)

    if n == 2: # niveau 2
        for x in range(5, width - 80, 80):
            addBrick(x + 37.5, 50, 1)
            addBrick(x + 37.5, 70, random.randint(1,3))
            addBrick(x + 37.5, 90, 1)
            addBrick(x + 37.5, 110, random.randint(1,3))
            addBrick(x + 37.5, 130, random.randint(1,2))
            addBrick(x + 37.5, 150, 1)
    if n == 3: # niveau 3
        for x in range(5, width - 80, 80):
            addBrick(x + 37.5, 50, 1)
            addBrick(x + 37.5, 70, random.randint(1,4))
            addBrick(x + 37.5, 90, random.randint(1,4))
            addBrick(x + 37.5, 110, 3)
            addBrick(x + 37.5, 130, random.randint(1,4))
            addBrick(x + 37.5, 150, random.randint(1,4))
            addBrick(x + 37.5, 170, 1)

    if n == 4: # niveau 4. Possible d'en ajouter indéfinitment!
        for x in range(5, width - 80, 80):
            addBrick(x + 37.5, 50, random.choice([1,4,5]))
            addBrick(x + 37.5, 70, random.randint(1,5))
            addBrick(x + 37.5, 90, random.randint(1,5))
            addBrick(x + 37.5, 110, random.choice([1,4,5]))
            addBrick(x + 37.5, 130, random.randint(1,5))
            addBrick(x + 37.5, 150, random.choice([1,4,5]))
            addBrick(x + 37.5, 170, random.randint(1,5))
            addBrick(x + 37.5, 190, random.choice([1,3,5]))
            addBrick(x + 37.5, 210, 1)
        
    
def setup():
    global paddle, ball, n # on déclare la variable paddle et ball comme globale
    paddle = Paddle() # on crée l'objet paddle
    ball = Ball() # on crée l'objet ball
    
    size(805,600) # définit la taille de la fenêtre de jeu
    global bg
    bg = loadImage("background.png") # on définit l'image de fond
    n = 0 # Le niveau 0 est le menu d'introduction
    
def affichageNiveau(n): # text en haut au centre qui dit sur quel niveau le joueur est
    s = 'Niveau ' + str(n) # str(n) étant la valeur n sous forme de string
    fill(255,255,255) # couleur du texte
    text(s, 400, 30) # taille et position du texte

def draw(): # fonction qui fait avancer le jeu
    global playingGame, n, score
    background(0,0,0) # fond noir
    fill(255,255,255)
    background(bg) # met image en arrière plan
    text("Frame rate: " + str(int(frameRate)), 80, 30) # afficher la quantité de "Frames Per Second"
    text("Score: ", 720, 30) # affichage du mot score
    text(str(int(score)),775, 30) # suivi du chiffre qui est actualisé constamment (il y a une manière plus efficace de l'écrire)
    affichageNiveau(n) # affiche le texte qui montre le niveau sur lequel on est
    jeff=0 # création de variable qui empêche plusieures briques d'être détruites simultanément
    #appel des méthodes pour le paddle
    paddle.display() # affiche le paddle
    if playingGame: # permet de vérifier si le paddle entre en collision avec la balle pendant que le jeu fonctionne
        paddle.checkEdges()
        paddle.update()
    #appel des méthodes pour la balle
    ball.display() 
    if playingGame: # permet de vérifier si la balle entre en collision avec les briques ou le paddle pendant que le jeu fonctionne
        ball.checkEdges()
        ball.update()
    if (ball.meetsP(paddle)): # si la balle rencontre le paddle
        if (ball.dir.y > 0): # si la position sur l'axe des ordonnées de la balle est supérieure à 0
            ball.dir.y *= -1 # invertit la vitesse sur l'axe des ordonnées
            paddle.w = 150 # largeur du paddle (pour reset un bonus)
            ball.vel = PVector(1.5, 1.5)*4 # vitesse de la balle (pour reset un bonus)
    for i in range(len(bricks)): # affiche les briques
        bricks[i].display()
    for i in range(len(bricks)-1,-1,-1):
        if (ball.meetsB(bricks[i])) and jeff==0: # si la balle rencontre une brique et la veriable est égale à 0
            if bricks[i].hits == 1: # si la couleur de la brique est la première du dictionnaire (même chose pour chaque if de ce type)
                bricks.pop(i)
                jeff = jeff+1 # assure que la balle ne détruit pas deux briques au même temps
                scoreAleatoire = random.randint(75,100) # ajoute au score du joueur au hasard un nombre entre 
                score = score+scoreAleatoire
                ball.dir.y *= random.uniform(-1,-1) #on change aleatoirement la direction de la balle
            elif bricks[i].hits == 2: # bonus
                r = random.randint(0,1) # choisit un chiffre au hasard entre 0 et 1
                if r == 0:
                    paddle.w = 500 # agrandit la taille du paddle
                    bricks.pop(i)
                    jeff = jeff+1
                    score = score+25
                    ball.dir.y *= random.uniform(-1,-1) #on change aleatoirement la direction de la balle
                elif r == 1:
                    ball.vel = PVector(0.5, 0.5)*4 # ralentit la balle
                    bricks.pop(i)
                    jeff = jeff+1
                    score = score+25
                    ball.dir.y *= random.uniform(-1,-1) #on change aleatoirement la direction de la balle
            elif bricks[i].hits == 3: # briques qui prennent deux coups pour être détruites
                bricks[i].hits = 1
                bricks[i].col = Brick.COLORS[1] # devenir brique détruisible en 1 coup
                jeff = jeff+1
                score = score+50
                ball.dir.y *= random.uniform(-1,-1) #on change aleatoirement la direction de la balle
            elif bricks[i].hits == 4: # briques qui prennent trois coups pour être détruites
                bricks[i].hits = 3
                bricks[i].col = Brick.COLORS[3] # devient brique destructible en 2 coups (récursivité)
                jeff = jeff+1
                score = score+33
                ball.dir.y *= random.uniform (-1,-1) #on change aleatoirement la direction de la balle
            elif bricks[i].hits == 5: # malus
                r = random.randint(0,1)
                if r == 0:
                    paddle.w = 50 # rétrécit le paddle
                    bricks.pop(i)
                    jeff = jeff+1
                    score = score-10
                    ball.dir.y *= random.uniform(-1,-1) #on change aleatoirement la direction de la balle
                elif r == 1:
                    ball.vel = PVector(2.0, 2.0)*4 # accélère la balle
                    bricks.pop(i)
                    jeff = jeff+1
                    score = score-10
                    ball.dir.y *= random.uniform(-1,-1) #on change aleatoirement la direction de la balle 

    if bricks == []: # si il ne reste plus de briques
        if n == 0: # et que on est au niveau 0
            playingGame = False
            fill(255,255,255)
            bg2 = loadImage("background2.png")
            background(bg2) # arrière plan
            textAlign(CENTER) # centre le texte
            textSize(65) # taille du texte
            text('Jeu du CASSE-BRIQUE', 400, 275) # titre
            textSize(20)
            text('Cliquez pour commencer (Controles: Q = Gauche et D = Droite)', 400, 325) # sous-titre
            textSize(15)
            text('Version Alpha 1.0', 735, 585)
            if mousePressed:
                n += 1 # passe au prochain niveau
                level(n) # affiche le niveau
        elif n == 4: # si c'est le dernier niveau
            playingGame = False
            fill(255,255,255)
            bg5 = loadImage("end.png")
            background(bg5)
            textAlign(CENTER)
            textSize(60)
            text('FIN', 400, 300)
            textSize(35)
            text('Votre score :', 375, 350)
            text(str(int(score)), 550, 350)
            textSize(60)
            if mousePressed:
                exit() # ferme la fenêtre de jeu
        else:
            playingGame = False
            textSize(80)
            fill(255,255,255)
            bg4 = loadImage("win.png")
            background(bg4)
            textAlign(CENTER)
            text('VICTOIRE', 400, 325)
            textSize(35)
            text('Cliquez pour le prochain niveau', 400, 375)
            textSize(20)
            if mousePressed:
                n += 1 # prochain niveau
                level(n)
    if ball.checkEdges() == 1: # si la balle n'est pas attrappée par le paddle
        playingGame = False
        textSize(60)
        fill(255,255,255)
        bg3 = loadImage("gameover.png")
        background(bg3)
        textAlign(CENTER)
        text('GAME OVER', 400, 300)
        textSize(20)
        text('Cliquez pour recommencer', 400, 325)
        if mousePressed:
            for i in range(len(bricks)-1,-1,-1):
                bricks.pop(i) # enlève toutes les briques (une sorte de reset)
            score = score - 1000 # pénalité
            if score < 0: # pour éviter d'avoir un score négatif
                score = 0
            level(n)

# détection des mouvements touches q et d
def keyPressed():
    if key == "q" or key == "Q": # mouvement
        paddle.isMovingLeft = True
    elif key == "d" or key == "D":
        paddle.isMovingRight = True
    elif key== "v" or key=="V":
        # Pour les Administarteurs, pour passer au prochain niveau
        for i in range(len(bricks)-1,-1,-1):
            bricks.pop(i)
        
#annulation des mouvements quand on relâche la touche
def keyReleased():
    paddle.isMovingRight = False
    paddle.isMovingLeft = False
