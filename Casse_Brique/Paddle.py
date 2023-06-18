# coding=utf-8  (obligatoire Python 2.7)

class Paddle():

    def __init__(self): # constructeur
        self.w = 150  # attribut longueur du paddle
        self.h = 15   # attribut largeur du paddle
        # la position du paddle avec un objet Pvector
        self.pos = PVector(width/2 - self.w/2, height - 40)
        self.isMovingLeft = False  # booléen pour mouvement à gauche
        self.isMovingRight = False  # idem à droite
        self.stepSize = 10   # pas pour le déplacement
    # méthode premettant l'affichage
    def display(self):
        fill("#ff9664") # couleur de remplissage
        noStroke()  # pas de "bord"
        # affichage du rectangle rect(x,y,longueur, largeur)
        rect(self.pos.x, self.pos.y, self.w, self.h)
    # méthode pour actualiser l'affichage des déplacements
    def update(self):
        if self.isMovingLeft:
            self.move(-self.stepSize)
        elif self.isMovingRight:
            self.move(self.stepSize)
     # méthode qui gère le déplacement   
    def move(self, step):
        self.pos.x +=step
    # méthode qui gère les collisions avec les bords
    def checkEdges(self):
        if self.pos.x <= 0:
            self.pos.x = 0
        elif self.pos.x + self.w >= width:
            self.pos.x = width - self.w
