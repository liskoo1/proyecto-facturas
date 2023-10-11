from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
import tkinter as tk
import pandas as pd
from db import Db
from suplier import interface_suplier as it
import delete

class body:
    def __init__(self) -> None:
        #Generate principal window
        self.root = Tk()
        self.proveedor = LabelFrame(self.root,padx=108,pady=305,background= "#5D6D7E", border=0 )
        self.select_button = LabelFrame(self.root, padx=110, pady=127,background= "#5D6D7E", border=0)
        self.data_text = Text(self.select_button, wrap= WORD, background="#CCD1D1")
        self.data = None
    def init_body(self):
        '''Create label and window of start '''
        #Create title
        self.root.title("RECONOCIMIENTO DE DATOS EN FACTURAS")
        #Inser icon of window
        self.root.iconbitmap("img/icono.ico")
        #Create label decoration
        Label(self.root, text="Nombre de la empresa",font=("Felix Titling",23,"bold"),bg= "#B2BABB",padx=439, pady=27 ).grid(row=1,column=1,columnspan=4)
        #Do size to principal window
        self.root.resizable(800,900)
        #Create the place of radiobutton
        self.proveedor.grid(row=2,column=1)
        # Show suplier
        self.data = Db().show_all_suplier()
        #Create label
        self.select_button.grid(row=2, column=3)


    def proveedores(self):

        '''Generate the Frame label for suplier and button'''

        self.data = Db().show_all_suplier() 
        # save the cif 
        cif = StringVar()

        def select():
            # extract cif 
            select = cif.get()
            
            return select
        
        for dato in self.data:
            # Create button new suplier
            Radiobutton(self.proveedor,pady=5,text=f"{dato['nombre']}",value= dato['cif'], variable= cif, bg="#5D6D7E").pack()
        try:
            Button(self.proveedor,font=("Harlow Solid",12,"bold"),cursor="hand2", text="Insertar proveedor nuevo",border=1,pady=10,bg= "#99A3A4", command= lambda: it.new_suplier(name_buttom="CREAR", win_proveedor= self.proveedor )).pack()    
            Button(self.proveedor,font=("Harlow Solid",12,"bold"),cursor="hand2", text="Eliminar proveedor",border=1,bg= "#99A3A4" ,pady=10, command=lambda: delete.delete_suplier(select(), self.proveedor)).pack()
            Button(self.proveedor,font=("Harlow Solid",12,"bold"),cursor="hand2", text="Modificar proveedor",border= 1,bg= "#99A3A4",pady=10, command=lambda: it.new_suplier(cif= select(), name_buttom="ACTUALIZAR",win_proveedor=self.proveedor)).pack()
            Button(self.proveedor,font=("Harlow Solid",12,"bold"),cursor="hand2",text="Seleccionar la factura"  ,border= 1,bg= "#99A3A4" ,pady=10,command= lambda: self.select_file(select(),last=True)).pack()
        except:
            pass
    
    
    def select_file(self, cif):
        '''Select image'''
        from suplier import interface_suplier
        #clean the label select_button
        interface_suplier().limpiar_labelframe(label=self.select_button, last= True)
        # get data of  the position description , iva , price ect
        lista_plantillas = Db().obtener_datos_plantilla(cif)
        # Open the facture in png or jpg
        image = filedialog.askopenfilename(initialdir="/",title="Selecionar archivo",filetypes=(("JPG","*.jpg"),("PNG","*.png")))
        if image:
            # Extract data of facture
            data = it.show_data(image, lista_plantillas[6:])
            #clean the window data_text
            self.data_text.delete("1.0",tk.END)
            #insert data in data_text
            self.data_text.insert("1.0",data.to_string(index=False))
            # create buttom by update stock
            Button(self.select_button,font=("Harlow Solid",12,"bold"),cursor="hand2",border=5,pady=10,bg= "#99A3A4", text="Actualizar stock", command= lambda: Db().insert_products(data,cif,self.data_text, self.select_button)).pack()
            
            return data

    def text_facturas(self):
        '''Create a place where insert data of dataframe'''
        # Create label and button
        Label(self.select_button,border=0,pady=10, text= "Selecciona la factura que quieras meter en base de datos \n ", font=("arial",15,"bold"),bg= "#5D6D7E").pack()
        self.data_text.pack()
        Label(self.select_button,font=("Harlow Solid",12,"bold"), border=0,pady=10,bg= "#5D6D7E", text="Datos a insertar en base de datos").pack()
        Button(self.select_button,font=("Harlow Solid",12,"bold"),cursor="hand2",border=5,pady=10,bg= "#99A3A4", text= "Modificar articulo", command=lambda:self.wind_mod_article()).pack()
        self.root.mainloop()
        

    def wind_mod_article(self):
        '''create the window to modify the articles'''

        # Clean the window data_text
        self.data_text.delete("1.0",tk.END)
        self.data_text
        #create a new window  to modify article
        mod_win = Toplevel()
        mod_win.title("Modificar articulo")
        Label(mod_win, text="Nombre del articulo").grid(row=0,column=0)
        nombre_art = Entry(mod_win, width=50,)
        nombre_art.insert(0,"")
        nombre_art.grid(row=0, column=1) 
        Button(mod_win, cursor="hand2",border=1,pady=10,text="MOSTRAR", command= lambda:self.search_article(nombre_art.get(),self.data_text,mod_win.destroy())).grid(row=1, columnspan=2)
    
    def search_article(self, nombre_art, widget,destroy):
        '''Search one article in database'''
        try:
            # call the function where push button "MOSTRAR"
            destroy
            # now search the article in database
            connect = Db().connect
            cursor = connect.cursor()
            cursor.execute(f'SELECT * FROM productos WHERE descripcion = "{nombre_art}";')
            article = [dato[0:5] for dato in cursor]
            article = list(article[0])
            datos = f"{article[0]}\n{article[1]}\n{article[2]}\n{article[3]}\n{article[4]}"
            #clean window for insert a new data
            widget.delete("1.0",tk.END)
            # inser new data
            widget.insert("2.0",datos)
            #and create button
            Button(self.select_button,font=("Harlow Solid",12,"bold"),cursor="hand2",border=5,pady=10,bg= "#99A3A4", text= "Actualizar articulo", command=lambda:Db().modify_article(self.data_text,self.select_button)).pack()
        except:
            pass
    
