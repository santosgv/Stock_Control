from tkinter import *

main=Tk()

class aplicacao():
    def __init__(self):
        self.main=main
        self.Principal()
        main.mainloop()

    def Principal(self):
        self.main.title('Planilha')
        self.main.geometry('1024x1024')
        
aplicacao()