#coding: utf-8
import tkinter as tk
import tkinter.font as tkFont
import json

class fenetre:
    def __init__(self, master):
        self.annee = ""
        self.groupe = ""

        self.master = master
        master.title('Update Course')
        master.geometry('800x800')
        
        font = tkFont.Font(size=15)
        #tous les label
        self.labelDateHeure = tk.Label(master, text="Date et Heure : ", font=font).place(x=340, y= 20)
        
        self.labelAnnee = tk.Label(master, text="Année").place(x=138, y=73)
        self.labelMois = tk.Label(master, text="Mois").place(x=380, y=73)
        self.labelJour = tk.Label(master, text="Jour").place(x=610, y=73)

        self.labelHeure = tk.Label(master, text="Heure").place(x=240, y=140)
        self.labelMinutes = tk.Label(master, text="Minutes").place(x=495, y=140)

        self.labelIntitule = tk.Label(master, text="Intitulé").place(x=370, y=220)

        self.labelProf = tk.Label(master, text="prof").place(x=370, y=275)
        
        #value d'entry
        self.valueAnnee = tk.StringVar()
        self.valueAnnee.set("AAAA")

        self.valueMois = tk.StringVar()
        self.valueMois.set("MM")

        self.valueJour = tk.StringVar()
        self.valueJour.set("JJ")

        #entry area
        self.entreeAnnee = tk.Entry(master, textvariable=self.valueAnnee, width=10).place(x=130, y = 100)
        self.entreeMois = tk.Entry(master, textvariable=self.valueMois, width=10).place(x=370, y=100)
        self.entreeJour = tk.Entry(master, textvariable=self.valueJour, width=10).place(x=600, y=100)

        #autre value
        self.valueHeure = tk.StringVar()
        self.valueHeure.set("HH")

        self.valueMinutes = tk.StringVar()
        self.valueMinutes.set("MiMi")

        self.valueIntitule = tk.StringVar()
        self.valueIntitule.set("Ecrire l'intitule ici")

        self.valueProf = tk.StringVar()
        self.valueProf.set("Prof")

        #entry area
        self.entreeHeure = tk.Entry(master, textvariable=self.valueHeure, width=10).place(x=230, y=170)
        self.entreeMinutes = tk.Entry(master, textvariable=self.valueMinutes, width=10).place(x=485, y=170)

        self.entreeIntitule = tk.Entry(master, textvariable=self.valueIntitule, width=40).place(x=280, y=250)

        self.entreeProf = tk.Entry(master, textvariable=self.valueProf, width=20).place(x=335, y = 295)

        #bouton accepter
        self.boutonAccepter = tk.Button(master, text="Accepter", command = self.MAJ).place(x=350, y = 700)

        self.liste = tk.Listbox(master)

        self.labelListe = tk.Label(master, text="Quel groupe ?").place(x=370, y=520)

        self.liste.insert(1, "TP1")
        self.liste.insert(2, "TP2")
        self.liste.insert(3, "TP3")
        self.liste.insert(4, "TP4")
        self.liste.insert(5, "TD1")
        self.liste.insert(6, "TD2")
        self.liste.insert(7, "CM")

        self.liste.place(x=330 , y=330)

    def MAJ(self):

        #récupération des données
        self.annee = self.valueAnnee.get()
        print(self.annee)

        self.mois = self.valueMois.get()
        print(self.mois)

        self.jour = self.valueJour.get()
        print(self.jour)

        self.heure = self.valueHeure.get()
        print(self.heure)

        self.minutes = self.valueMinutes.get()
        print(self.minutes)

        self.intitule = self.valueIntitule.get()
        print(self.intitule)

        self.prof = self.valueProf.get()

        self.groupe = self.liste.get(self.liste.curselection())
        print(self.groupe)

        data = {f'{self.annee}-{self.mois}-{self.jour}-{self.heure}-{self.minutes}':[{'nom': self.intitule, 'prof': self.prof, 'heure': f'{self.heure}:{self.minutes}', 'groupe': self.groupe}]}
        jstr = json.dumps(data, indent=4)

        print(jstr)
        with open('data1.json', 'a') as f:
            json.dump(data, f, indent=4)
        

        




if __name__ == "__main__":
    # execute only if run as a script

    root = tk.Tk()
    window = fenetre(root)
    root.mainloop()
