import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


#---- création de l'interface ----
fenetre = tk.Tk() 
fenetre.title("Tableau")


#--------- fonction d'Ajouter_info ----------
def Ajouter_info():

    Name = Name_input.get() 
    Age = Age_input.get() 
    Ville = Ville_input.get() 

    if Name and Age and Ville: 
        Tableau.insert("", "end", values=(Name, Age, Ville))

    else:
        messagebox.showwarning("Champs vides", "Veuillez remplir tous les champs avant d'ajouter.")


#------------ Name label | name input -------------
Name_label = tk.Label(fenetre, text="Entrer le Nom : ")
Name_label.pack()
Name_input = tk.Entry(fenetre)
Name_input.pack()


#------------ Age label | Age input -------------
Age_label = tk.Label(fenetre, text="Ajouter Votre Age :")
Age_label.pack()
Age_input = tk.Entry(fenetre)
Age_input.pack()


#------------ Ville label | Ville input -------------
Ville_label = tk.Label(fenetre, text="Ajouter la ville : ")
Ville_label.pack()
Ville_input = tk.Entry(fenetre)
Ville_input.pack()


#-------------------- button d'Ajoute --------------------
button_ajouter = tk.Button(fenetre, text="Ajouter Informations", command=Ajouter_info)
button_ajouter.pack(pady=10)



#--------------- Création de Tableau -------------------
colonnes = ("Nom", "Age", "Ville")
Tableau = ttk.Treeview(fenetre, columns=colonnes, show="headings")

Tableau.pack()


#------- l'Entete de Tableau ---------
Tableau.heading("Nom", text="Nom")
Tableau.heading("Age", text="Age")
Tableau.heading("Ville", text="Ville")


#------- Columns de Tableau ---------
Tableau.column("Nom", width=100, anchor="center")
Tableau.column("Age", width=50, anchor="center")
Tableau.column("Ville", width=100, anchor="center")


donnes = []


for element in donnes:
    Tableau.insert("", "end", values=element)


fenetre.mainloop()
