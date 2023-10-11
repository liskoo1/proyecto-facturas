import mysql.connector
from tkinter import messagebox
import tkinter as tk



class Db:
    def __init__(self) -> None:
        self.connect =  mysql.connector.connect(user = "root",password = "ktmexc200",host = "localhost", database = "tienda")
        self.cursor = self.connect.cursor()

    def insert_suplier_db(self,name, cif, category,address, phone, email):
        ''' connect to db and insert the data of suplier'''
        
        try:
            # Execute Query
            self.cursor.execute(f'INSERT INTO proveedores(nombre, cif, categoria, direccion, telefono, email) VALUES ("{name}", "{cif}","{category}", "{address}", {int(phone)}, "{email}");')
            self.connect.commit()
        except:
            self.cursor.execute(f'INSERT INTO proveedores(nombre, cif, categoria, direccion, telefono, email) VALUES ("{name}", "adwada","{category}", "{address}", {0}, "{email}");')
            self.connect.commit()
            messagebox.showerror("Error","Has introducido algun dato erroneo o hay campos vacios. Vuelve a modificarlos atraves del boton Modificar Proveedor")
            messagebox.showinfo("Info", "RECUERDA!! Proveedor: El campo de telefono debe de ser numeros ")

    def insert_tamplate_description(self, x1_descrip, y1_descrip, x2_descrip, y2_descrip):
        try: 
            ''' connect to db and insert the data of tamplate_description''' 
            # Execute Query
            self.cursor.execute(f'INSERT INTO plantilla_descripcion(x1_descrip, y1_descrip, x2_descrip, y2_descrip) VALUES ({int(x1_descrip)}, {int(y1_descrip)}, {int(x2_descrip)}, {int(y2_descrip)});')
            

        except:
            self.cursor.execute(f'INSERT INTO plantilla_descripcion(x1_descrip, y1_descrip, x2_descrip, y2_descrip) VALUES ({0}, {0}, {0}, {0});')
            messagebox.showerror("Error","Has introducido algun dato erroneo o hay campos vacios. Vuelve a modificarlos atraves del boton Modificar Proveedor")
            messagebox.showinfo("Info", "RECUERDA!! Descripción: Los campos de los ejes X e Y deben de ser numeros ")

    
    def insert_tamplate_iva(self, x1_iva,y1_iva,x2_iva,y2_iva):
        ''' connect to db and insert the data of tamplate_iva'''
        try:
            # Execute Query
            self.cursor.execute(f'INSERT INTO plantilla_iva(x1_iva, y1_iva, x2_iva, y2_iva) VALUES ({int(x1_iva)}, {int(y1_iva)}, {int(x2_iva)}, {int(y2_iva)});')
            

        except:
            self.cursor.execute(f'INSERT INTO plantilla_iva(x1_iva, y1_iva, x2_iva, y2_iva) VALUES ({0}, {0}, {0}, {0});')
            messagebox.showerror("Error","Has introducido algun dato erroneo o hay campos vacios. Vuelve a modificarlos atraves del boton Modificar Proveedor")
            messagebox.showinfo("Info", "RECUERDA!! Iva: Los campos de los ejes X e Y deben de ser numeros ")


    def insert_tamplate_totales(self,x1_totales,y1_totales,x2_totales,y2_totales):
        ''' connect to db and insert the data of tamplate_totales'''
        try:
            # Execute Query
            self.cursor.execute(f'INSERT INTO plantilla_totales(x1_totales, y1_totales, x2_totales, y2_totales) VALUES ({int(x1_totales)}, {int(y1_totales)}, {int(x2_totales)}, {int(y2_totales)});')

        except: 
            self.cursor.execute(f'INSERT INTO plantilla_totales(x1_totales, y1_totales, x2_totales, y2_totales) VALUES ({0}, {0}, {0}, {0});')
            messagebox.showerror("Error","Has introducido algun dato erroneo o hay campos vacios. Vuelve a modificarlos atraves del boton Modificar Proveedor")
            messagebox.showinfo("Info", "RECUERDA!! Totales: Los campos de los ejes X e Y deben de ser numeros  ")


    def insert_tamplate_prices(self,x1_precios,y1_precios,x2_precios,y2_precios):
        ''' connect to db and insert the data of tamplate_prices'''
        try:
            # Execute Query
            self.cursor.execute(f'INSERT INTO plantilla_precios(x1_precios, y1_precios, x2_precios, y2_precios) VALUES ({int(x1_precios)}, {int(y1_precios)}, {int(x2_precios)}, {int(y2_precios)});')
            
        except:
            self.cursor.execute(f'INSERT INTO plantilla_precios(x1_precios, y1_precios, x2_precios, y2_precios) VALUES ({0}, {0}, {0}, {0});')
            messagebox.showerror("Error","Has introducido algun dato erroneo o hay campos vacios. Vuelve a modificarlos atraves del boton Modificar Proveedor")
            messagebox.showinfo("Info", "RECUERDA!! Price: Los campos de los ejes X e Y deben de ser numeros  ")


    def insert_tamplate_units(self,x1_unidades,y1_unidades,x2_unidades,y2_unidades):
        ''' connect to db and insert the data of tamplate_units'''
        try:
            # Execute Query
            self.cursor.execute(f'INSERT INTO plantilla_unidades(x1_unidades, y1_unidades, x2_unidades, y2_unidades) VALUES ({int(x1_unidades)}, {int(y1_unidades)}, {int(x2_unidades)}, {int(y2_unidades)});')
            # Make commit 
            self.connect.commit()
        except:

            self.cursor.execute(f'INSERT INTO plantilla_unidades(x1_unidades, y1_unidades, x2_unidades, y2_unidades) VALUES ({0}, {0}, {0}, {0});')
            self.connect.commit()
            messagebox.showerror("Error","Has introducido algun dato erroneo o hay campos vacios. Vuelve a modificarlos atraves del boton Modificar Proveedor")
            messagebox.showinfo("Info", "RECUERDA!! units : Los campos de los ejes X e Y deben de ser numeros  ")
        return self.connect


    def take_id_last_template(self):
        self.cursor.execute('SELECT id_plantilla_desc FROM plantilla_descripcion;')
        for dato in self.cursor:
            data = dato
        return data
    

    def show_all_suplier(self):
        ''' Show the suplier in the initial window'''
        
        self.cursor.execute('SELECT * FROM proveedores;')
        lista = [{"nombre": dato[0],"cif": dato[1],"categoria": dato[2],"direccion":dato[3],"telefono":dato[4],"email":dato[5]} for dato in self.cursor]

        self.connect.commit()
  
        return lista
    
    def update_data(self, cif ,list_data):


        self.cursor.execute(f'SELECT id_plantillas FROM proveedores WHERE cif = "{cif}";')

        id_plantilla = [dato[0] for dato in self.cursor]

        print(id_plantilla[0])
           
        try:
            '''Execute all instruction by modify the data of suplier in data base '''
            #DATOS
            if list_data[0]:
                self.cursor.execute(f'UPDATE proveedores SET nombre = "{list_data[0]}" WHERE cif = "{list_data[1]}";')

            if list_data[1]:
                self.cursor.execute(f'UPDATE proveedores SET cif = "{list_data[1]}" WHERE cif = "{list_data[1]}";')

            if list_data[2]:
                self.cursor.execute(f'UPDATE proveedores SET categoria = "{list_data[2]}" WHERE  cif = "{list_data[1]}";')

            if list_data[3]:
                self.cursor.execute(f'UPDATE proveedores SET direccion = "{list_data[3]}" WHERE cif = "{list_data[1]}";')

            if list_data[4]:
                self.cursor.execute(f'UPDATE proveedores SET telefono = {int(list_data[4])} WHERE  cif = "{list_data[1]}";')

            if list_data[5]:
                self.cursor.execute(f'UPDATE proveedores SET email = "{list_data[5]}" WHERE  cif = "{list_data[1]}";')
            # DESCRIPCION
            if list_data[6] :
                self.cursor.execute(f'UPDATE plantilla_descripcion SET x1_descrip = {int(list_data[6])} WHERE id_plantilla_des = "{id_plantilla[0]}" ;')
            
            if list_data[7]:
                self.cursor.execute(f'UPDATE plantilla_descripcion SET y1_descrip = {int(list_data[7])} WHERE id_plantilla_des = "{id_plantilla[0]}" ;')
            
            if list_data[8]:
                self.cursor.execute(f'UPDATE plantilla_descripcion SET x2_descrip = {int(list_data[8])} WHERE id_plantilla_des = "{id_plantilla[0]}" ;')
            
            if list_data[9]:
                self.cursor.execute(f'UPDATE plantilla_descripcion SET y2_descrip = {int(list_data[9])} WHERE id_plantilla_des = "{id_plantilla[0]}" ;')
            # IVA
            if list_data[10]:
                self.cursor.execute(f'UPDATE plantilla_iva SET x1_iva = {int(list_data[10])} WHERE id_plantilla_iva = "{id_plantilla[0]}" ;')
            
            if list_data[11]:
                self.cursor.execute(f'UPDATE plantilla_iva SET y1_iva = {int(list_data[11])} WHERE id_plantilla_iva = "{id_plantilla[0]}";')
            
            if list_data[12]:
                self.cursor.execute(f'UPDATE plantilla_iva SET x2_iva = {int(list_data[12])} WHERE id_plantilla_iva = "{id_plantilla[0]}";')
            
            if list_data[13]:
                self.cursor.execute(f'UPDATE plantilla_iva SET y2_iva = {int(list_data[13])} WHERE id_plantilla_iva = "{id_plantilla[0]}";')
            
            # TOTALES
            if list_data[14]:
                self.cursor.execute(f'UPDATE plantilla_totales SET x1_totales = {int(list_data[14])} WHERE id_plantilla_totales = "{id_plantilla[0]}" ;')
            
            if list_data[15]:
                self.cursor.execute(f'UPDATE plantilla_totales SET y1_totales = {int(list_data[15])} WHERE id_plantilla_totales = "{id_plantilla[0]}" ;')
            
            if list_data[16]:
                self.cursor.execute(f'UPDATE plantilla_totales SET x2_totales = {int(list_data[16])} WHERE id_plantilla_totales = "{id_plantilla[0]}";')
            
            if list_data[17]:
                self.cursor.execute(f'UPDATE plantilla_totales SET y2_totales = {int(list_data[17])} WHERE id_plantilla_totales = "{id_plantilla[0]}" ;')

            # PRECIOS
            if list_data[18]:
                self.cursor.execute(f'UPDATE plantilla_precios SET x1_precios = {int(list_data[18])} WHERE id_plantilla_precios = "{id_plantilla[0]}" ;')
            
            if list_data[19]:
                self.cursor.execute(f'UPDATE plantilla_precios SET y1_precios = {int(list_data[19])} WHERE id_plantilla_precios = "{id_plantilla[0]}" ;')
            
            if list_data[20]:
                self.cursor.execute(f'UPDATE plantilla_precios SET x2_precios = {int(list_data[20])} WHERE id_plantilla_precios = "{id_plantilla[0]}" ;')
            
            if list_data[21]:
                self.cursor.execute(f'UPDATE plantilla_precios SET y2_precios = {int(list_data[21])} WHERE id_plantilla_precios = "{id_plantilla[0]}" ;')
            
            # UNIDADES
            if list_data[22]:
                self.cursor.execute(f'UPDATE plantilla_unidades SET x1_unidades = {int(list_data[22])} WHERE id_plantilla_unidades = "{id_plantilla[0]}";')
            
            if list_data[23]:
                self.cursor.execute(f'UPDATE plantilla_unidades SET y1_unidades = {int(list_data[23])} WHERE id_plantilla_unidades = "{id_plantilla[0]}";')
            
            if list_data[24]:
                self.cursor.execute(f'UPDATE plantilla_unidades SET x2_unidades = {int(list_data[24])} WHERE id_plantilla_unidades = "{id_plantilla[0]}";')
            
            if list_data[25]:
                self.cursor.execute(f'UPDATE plantilla_unidades SET y2_unidades = {int(list_data[25])} WHERE id_plantilla_unidades = "{id_plantilla[0]}";')
            self.connect.commit()
        except:
                    messagebox.showerror("Error","Has introducido algun dato erroneo")
                    messagebox.showinfo("Info", "RECUERDA!! : El campo de telefono y los campos de los ejes X e Y deben de ser numeros ")
            
    def modify_article(self,data_text,label):
        import suplier
        descipcion = data_text.get("1.0",tk.END)
        lista_item = descipcion.split("\n")
        self.cursor.execute(f'UPDATE productos SET descripcion = "{lista_item[1]}", unidades = {int(lista_item[2])}, precio = {float(lista_item[3])}, iva = {float(lista_item[4])} WHERE id = {int(lista_item[0])}')
        self.connect.commit()
        data_text.delete("1.0",tk.END)
        data_text.insert("1.0","\n\n\n\n\n\n\n\n\n\n\n                    ARTICULO ACTIALIZADO CORRECTAMENTE!!!           ")
        suplier.interface_suplier().limpiar_labelframe(label, last=True)
        print(lista_item)
        
        

    def obtener_datos_plantilla(self, cif):

        '''Here, we extract the x and y axes that are in database '''

        self.cursor.execute(f'SELECT id_plantillas FROM proveedores WHERE cif = "{cif}";')

        id_plantilla = [dato[0] for dato in self.cursor]
        print(id_plantilla)

        self.cursor.execute(f'SELECT nombre, cif, categoria, direccion, telefono, email FROM proveedores WHERE id_plantillas = {id_plantilla[0]};')
        data_suplier = [dato for dato in self.cursor]

    # Descripcion

        self.cursor.execute(f'SELECT x1_descrip, y1_descrip, x2_descrip, y2_descrip FROM plantilla_descripcion WHERE id_plantilla_des = {id_plantilla[0]};')
        descrip = [dato for dato in self.cursor]
 

    # IVA
        self.cursor.execute(f'SELECT x1_iva, y1_iva, x2_iva, y2_iva FROM plantilla_iva WHERE id_plantilla_iva = {id_plantilla[0]};')
        iva = [(dato) for dato in self.cursor]

    # PRECIOS

        self.cursor.execute(f'SELECT x1_precios, y1_precios, x2_precios, y2_precios FROM plantilla_precios WHERE id_plantilla_precios = {id_plantilla[0]};')
        precios = [dato for dato in self.cursor]
     
    # TOTALES

        self.cursor.execute(f'SELECT x1_totales, y1_totales, x2_totales, y2_totales FROM plantilla_totales WHERE id_plantilla_totales = {id_plantilla[0]};')
        totales = [dato for dato in self.cursor]
        print(totales)
    # UNIDADES

        self.cursor.execute(f'SELECT x1_unidades, y1_unidades, x2_unidades, y2_unidades FROM plantilla_unidades WHERE id_plantilla_unidades = {id_plantilla[0]};')
        unidades = [dato for dato in self.cursor]
        lista = [data_suplier,descrip,iva,totales,precios,unidades]
        lista2 = []
        for elemento in lista:
            for elemento2 in elemento:
                for elemento3 in elemento2:
                    lista2.append(elemento3)
        
        return lista2
    
    def insert_products(self,df, cif, data_text, label):
        ''' insert products in db'''
        import suplier

        self.connect
        for i in range (len(df)) :
            print(df.iloc[i])
            self.cursor.execute(f'SELECT descripcion FROM productos WHERE descripcion = "{df.iloc[i][0]}";')
            item = [dato[0] for dato in self.cursor]
            
            if df.iloc[i][0] in item:
                self.cursor.execute(f'UPDATE productos SET unidades = unidades + {int(df.iloc[i][2])} WHERE descripcion = "{item[0]}";')
                self.connect.commit()
            else:
                self.cursor.execute(f'INSERT INTO productos(descripcion, unidades, precio, iva, cif_proveedor) VALUES ("{df.iloc[i][0]}",{int(df.iloc[i][2])},{float(df.iloc[i][3])},{float(df.iloc[i][1])},"{cif}");')
                self.connect.commit()
        data_text.delete("1.0",tk.END)
        data_text.insert("1.0","\n\n\n\n\n\n\n\n\n\n\n                    STOCK ACTIALIZADO CORRECTAMENTE!!!           ")
        suplier.interface_suplier().limpiar_labelframe(label, last=True)
    def list_cif(self, cif):
        ''' create a list of all cif in data base'''

        self.connect
        self.cursor.execute(f'SELECT cif FROM proveedores WHERE cif = "{cif}";')
        item = [dato[0] for dato in self.cursor]
        return item