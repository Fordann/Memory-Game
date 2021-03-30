from tkinter import *
import random
import time

#Initialisation de la fenetre
fenetre=Tk()
fenetre.title("MLG meme memory")
fenetre.geometry("2000x2000")

#Initialisation d'interface
fond_menu=Canvas(fenetre,height=2000,width=2000,bg='red')
fond_menu.pack(side=LEFT)

fond_choisir_niveau=Canvas(fenetre,height=2000,width=2000,bg='blue')
fond_choisir_niveau.pack(side=LEFT)

fond_memory=Canvas(fenetre,height=2000,width=2000,bg='white')
fond_memory.pack(side=LEFT)

#Chargement d'une image global
img1 = PhotoImage(file = "dos_de_carte.gif")

#Initialisation du score
mytext = fond_memory.create_text(1750,200 ,text = 'Score : 00', fill = 'black', font = 'Arial 32')
mon_score=[0]

#Stockage de toute les images dans des listes associées
ensemble_image_possible = ["catzilla.gif","safe_image.gif","grenouille.gif","lion.gif","zèbre.gif","singe.gif"]
ensemble_image_animaux = ["lion.gif","zèbre.gif","singe.gif","tigre.gif","elephant.gif","ecureuil.gif"]
ensemble_image_bizarre = ["catzilla.gif","safe_image.gif","grenouille.gif","mickey.gif","chevalindon.gif","bebe.gif"]

#Liste permettant le stockage des images choisits
image_choisit=[]

#Stockage des référence des images
stockage_des_images = {}
bouton_liste=[]

#Stockage des des images que l'utilisateurs veut retourner
stockage_clique=[]

def menu():
    #Mise en page des boutons
    bouton_menu = Button(fenetre, text="Jouer", height=10, width=50, anchor=CENTER, command =choisir_niveau)
    fond_menu.create_window(1000,300, window=bouton_menu)


def choisir_niveau():
    #Destruction de l'ancienne fenetre
    fond_menu.destroy()

    #Mise en page des boutons
    bouton_image_animaux = Button(fenetre, text="Image d'animaux", height=10, width=50, anchor=CENTER, command = lambda parametre = "animaux":memory(parametre))
    fond_choisir_niveau.create_window(1000,200, window=bouton_image_animaux)

    bouton_image_bizarre = Button(fenetre, text="Image bizzare", height=10, width=50, anchor=CENTER, command = lambda parametre = "bizarre":memory(parametre))
    fond_choisir_niveau.create_window(1000,500, window=bouton_image_bizarre)

    bouton_aleatoire = Button(fenetre, text="Image aléatoire", height=10, width=50, anchor=CENTER, command = lambda parametre = "pas_de_parametre":memory(parametre))
    fond_choisir_niveau.create_window(1000,800, window=bouton_aleatoire)

def memory(choix_catégorie_image):
    #Destruction de l'ancienne fenetre
    fond_choisir_niveau.destroy()

    #Choix aléatoire d'images en fonction de la catégorie choisit par l'utilisateur
    selection_image(choix_catégorie_image)

    #Affichage des images
    afficher_image_bouton(image_choisit)

def selection_image(choix_catégorie_image):
    image_a_choisir = ensemble_image_possible

    if choix_catégorie_image == "animaux":
        image_a_choisir = ensemble_image_animaux
    elif choix_catégorie_image == "bizarre":
        image_a_choisir = ensemble_image_bizarre

    while len(image_choisit) != 12:
        #On choisit 6 images aléatoires dans la banque d'images
        choix_aleatoire=random.choice(image_a_choisir)
        if choix_aleatoire not in image_choisit:
            image_choisit.append(choix_aleatoire)
            image_choisit.append(choix_aleatoire)
    random.shuffle(image_choisit)

def afficher_image_bouton(image):
    nbre_colonne=0
    nbre_ligne=0
    for index,element in enumerate(image):
        if nbre_colonne==4:
            nbre_ligne+=1
            nbre_colonne=0

        #On stocke les images
        stockage_des_images["image"+str(index)] = img1

        #Puis on stocke les boutons
        bouton_liste.append(Button(fond_memory,image=img1, command = lambda parametre = index:stocker_image_clique(parametre)))

        #On met notre bouton sur un fond et on lui donne des coordonnées
        fond_memory.create_window(nbre_colonne*400+200,nbre_ligne*320+160, window=bouton_liste[index])
        nbre_colonne+=1

def stocker_image_clique(emplacement_bouton):
    #Stockage des coordonnées du bouton
    stockage_clique.append( emplacement_bouton )

    #On charge l'image relative au bouton
    img = PhotoImage(file = image_choisit[emplacement_bouton])

    #On stocke les référence de l'image
    stockage_des_images[str(emplacement_bouton)] = img

    #On test si l'utilisateur a sélectionné 1 ou 2 images
    if len( stockage_clique ) == 1:

        #On change l'image du bouton pour afficher l'image "cachée"
        bouton_liste[stockage_clique[0]]["image"]=img

    if len(stockage_clique) == 2:
        bouton_liste[stockage_clique[1]]["image"]=img

        #On actualise la fenetre pour faire apparaitre les modifications de l'image
        fenetre.update()
        comparer_image_clique()

        #On supprime les deux anciens choix de l'utilisateur
        del stockage_clique[:]

def comparer_image_clique():
    if stockage_clique[0] != stockage_clique[1]:
        #On compare les 2 images : si elles sont pareille les images sont désactivées pour rester affichées, si elles sont différentes les images sont rechangées en dos de carte
        if image_choisit[stockage_clique[0]] != image_choisit[stockage_clique[1]]:
            time.sleep(1)
            bouton_liste[stockage_clique[0]]["image"]=img1
            bouton_liste[stockage_clique[1]]["image"]=img1

        else:
            bouton_liste[stockage_clique[0]]["state"]=DISABLED
            bouton_liste[stockage_clique[1]]["state"]=DISABLED

            #On ajoute +10 au score
            mon_score[0]+=10
            fond_memory.itemconfig(mytext, text='Score : '+str(mon_score[0]))

#Lancement du memory
menu()

fenetre.mainloop()


