import tkinter
import os
import webbrowser
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
#code Name : Designe Sun 
#Build:205
#Name:PhenixPad X
"""
Version RC (REALSE CANDIDAT) VERSION PEUT ETRE INSTABLE OU PEUT CONTENIR DES INCOMPATIBILITE 
"""
class Notepad:

    #variables
    __root = Tk()

    #default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFichierMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditionMenu = Menu(__thisMenuBar,tearoff=0)
    __thisAideMenu = Menu(__thisMenuBar,tearoff=0)
    __thisUpdate = Menu(__thisMenuBar,tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self,**kwargs):
        #initialization

        #set icon
        try:
                self.__root.wm_iconbitmap("Notepad.ico") #GOT TO FIX THIS ERROR (ICON)
        except:
            pass 
                

        #set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            print("Error please to restart")
           

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            print("Error please to restart")
            

        #set the window text
        self.__root.title("Nouveaux Fichier - PhenixPad X : Béta Test Prewie")
            
        #center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight /2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        #to make the textarea auto resizable
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        #add controls (widget)

        self.__thisTextArea.grid(sticky=N+E+S+W)

        self.__thisFichierMenu.add_command(label="Nouveaux",command=self.__newFile)
        self.__thisFichierMenu.add_command(label="Ouvrir",command=self.__openFile)
        self.__thisFichierMenu.add_command(label="Sauvegarder",command=self.__saveFile)
        self.__thisMenuBar.add_cascade(label="Fichier",menu=self.__thisFichierMenu)
        

        self.__thisEditionMenu.add_command(label="Couper",command=self.__cut)
        self.__thisEditionMenu.add_command(label="Copier",command=self.__copy)
        self.__thisEditionMenu.add_command(label="Coller",command=self.__paste)
        self.__thisEditionMenu.add_command(label="Annuler",command=self.__Annuler)
        self.__thisEditionMenu.add_command(label="Rétablir",command=self.__Rétablir)
        self.__thisEditionMenu.add_separator()
        self.__thisEditionMenu.add_command(label="Exit",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="Edition",menu=self.__thisEditionMenu)
       
        self.__thisAideMenu.add_command(label="A propos de PhenixPad X",command=self.__showAbout)
        self.__thisAideMenu.add_command(label="contrat d'utilisation de PhenixPad X",command=self.__showAbout4)
        self.__thisAideMenu.add_command(label="Comment se procurez les mise a jour",command=self.__showAbout5)
        self.__thisAideMenu.add_command(label="Remontez un Bug",command=self.__showAbout6)
        self.__thisMenuBar.add_cascade(label="Aide",menu=self.__thisAideMenu)

       


        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT,fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    
        
    def __quitApplication(self):
        self.__root.destroy()
        showinfo("Message Important","vous etez entrain de utiliser une version de test il est deconsieller de l'utiliser au quotidien car dans c'ette version tout bug ou probléme trouvée ne sera pas coriger dans c'ette version et deviendra obselétte  mais elle le seront dans la version stable , c'est pour sa il et necesaire de migrée dans la version stable des quelle sera sortie .")

    def __showAbout(self):
        showinfo("A propos de PhenixPad X","Created by: Sloopy :Phenixpad X Version Dev : Facile à utiliser, nous avons conçu Phenixpad X avec des fonctionnalités utiles. Il sera mis à jour chaque mois pour améliorer l'utilisation du phenixpad X. N'oubliez pas de toujours le mettre à jour pour bénéficier des dernières améliorations. Tous droits réservés.\n Ce produit est fourni selon les termes du contrat de logiciel fourni par sloppy.\nCeci et une version de test de l application Phenixpad X il peut avoir des erreur\n crée par sloppy.")
    def __showAbout4(self):
          showinfo("contrat d'utilisation de PhenixPad X","TERME DU CONTRAT LOGICIEL SLOPPY FOURNIT AUX PHENIX PAD X:Le logiciel est protégez par le groupe sloppy ,c'est le groupe sloppy qui se charge du devellopment et de l amelioration de l aplication.\n sloppy ce chargera de faire dans l aplication:\n . Les mise a jour,J'usqua sa fin du support.\nAssurez l amelioration du produit.\nAssurez les correction de bug trouvée dans le produit.\nAssurez le service technique  d aide si un utlisateur recontre des probleme d utilisation de l aplication.\ncondition d instalation du logiciel :nous fournisson le logiciel gratuitement , il n ya pas de restricion d installation  par nombre d'ordinateur , vous pouvez deployez le logiciel sur tout votre parc informatique.")
    def __showAbout5(self):
          showinfo("Comment se procurez les mise a jour","Phenixpad X est un produit qui sera mise a jour chaque mois\n , pour vous offrir la meilleur expérience  d'utilisation de se logiciel\n , ces mise a jour vont permettre a résoudre tous les bug trouvée dans le logiciel\n , ainsi que lui intégrée de nouvelle fonctionnalité\n , et facilitée son utilisation\n. C'est pour ça que nous voulons que vous ayez la dernier\n version pour que vous pouvez profitez de la meilleur expérience du produit\n . Pour que vous pouvez vous procurez les dernière version\n , veuillez vous rendre sur notre site OFFICIEL de téléchargement pour la version en .EXE .")
    def __showAbout6(self):
        showinfo("Report Bug","Si vous avez trouvez un bug sur le logiciel merci de bien nous mettre au courant via ce mail : PhenixDeveloppement85@gmail.com\nC'est a grâce de votre fidélité quand n' améliore Phenixpad.")
    


    def __openFile(self):
        
        self.__file =  askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*")])
        showinfo("Message Important","vous etez entrain de utiliser une version de test il est deconsieller de l'utiliser au quotidien car dans c'ette version tout bug ou probléme trouvée ne sera pas coriger dans c'ette version et deviendra obselétte  mais elle le seront corigée dans la version stable , c'est pour sa il et necesaire de migrée dans la version stable des quelle sera sortie .")
        if self.__file == "":
            #no file to open
            self.__file = None
        else:
            

            #try to open the file 

            #set the window title
            self.__root.title(os.path.basename(self.__file) + " - PhenixPad X")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())

            file.close() 
           
        
    def __newFile(self):
        self.__root.title("Sans Titre - PhenixPad X")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):
       
        if self.__file == None:
            #save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            showinfo("Message Important","vous etez entrain de utiliser une version de test il est deconsieller de l'utiliser au quotidien car dans c'ette version tout bug ou probléme trouvée ne sera pas coriger dans c'ette version et deviendra obselétte  mais elle le seront corigée dans la version stable , c'est pour sa il et necesaire de migrée dans la version stable des quelle sera sortie .")
            if self.__file == "":
                self.__file = None
                

                
            else:
                #try to save the file
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                #change the window title
                self.__root.title(os.path.basename(self.__file) + " - PhenixPad X")
                
            
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")
        
    def __Annuler(self):
        self.content.edit_undo()

    def __Rétablir(self):
        self.content.edit_redo()

    def run(self):

        #run main application
        self.__root.mainloop()




#run main application
notepad = Notepad(width=600,height=400)
notepad.run()