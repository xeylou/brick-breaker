from tkinter import *
from random import randint

touches = set()

def enfoncer(event):
    touches.add(event.keysym)

def relacher(event):
    try:
        touches.remove(event.keysym)
    except:
        pass
# ses deux fonctions sont pour la fluidité

def action():
    global dbx, dby
    balle = c.coords(b)
    raquette = c.coords(r)

    if "Left" in touches and c.coords(r)[0] > 0:   # si flèche gauche pressée déplacement
        c.move(r, -10, 0)

    if "Right" in touches and c.coords(r)[2] < 800:
        c.move(r, 10, 0)

    if balle[2] >= 800:   # si balle trop à droite
        dbx = -pas

    if balle[0] <= 0:   # si balle trop à gauche
        dbx = pas

    if balle[3] >= 600:   # si la balle passe en dessous de la fenêtre visible
        print('Vous avez perdu')
        f.destroy()

    if balle[1] <= 0:
        dby = pas

    if (balle[0] + balle[2])/2>=raquette[0] and (balle[0]+balle[2])/2<=raquette[2] and balle[3]>=raquette[1]:
        dby = -pas
    # collisions

    c.move(b, dbx, dby)
    f.after(25, action)
    # déplacement balle

    coll = c.find_overlapping(*balle)  # contact balle brique
    if len(coll) >= 2:
        if coll[1] == 2:   # contact avec barre
            pass
        if coll[1] > 2:    # contact avec brique
            print(coll[1])
            c.delete(coll[1])
            dby = pas

def creation_briques():
    #balle = c.coords(b)
    #print(balle)
    x = 22
    y = 40
    brique = []
    #Lb = []
    couleur = ['red','blue']

    while x < 740:
        tmp=0
        brique.append([c.create_rectangle(x, y, x + 61, y + 20, fill=couleur[tmp])])
        #Lb.append((x, y))
        y += 21
        if y >= 180:
            x += 62
            y = 40
            tmp=-1
            


f = Tk()                                                                                # création fenêtre
c = Canvas(f, bg='black', width=800, height=600)                                        # création fond
c.pack()                                                                                # remplissage fenêtre avec fond
r = c.create_rectangle(1300, 590, 450, 590, fill="white", width=6, outline="white")      # création rectangle
b = c.create_oval(300, 200, 310, 210, fill="green", outline="Gold")                     # création balle

# -variables-#
pas = 6   # vitesse de déplacement de la balle
dbx, dby = pas, pas

action()                            # lancement du jeu
creation_briques()                  # création briques
f.bind('<KeyPress>', enfoncer)
f.bind('<KeyRelease>', relacher)

f.mainloop()