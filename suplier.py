from tkinter import *
from tkinter.messagebox import *
from reconocimiento_texto import * 
from db import Db
import delete

class interface_suplier:       
    def new_suplier(name_buttom: str , win_proveedor,cif: str = "" ):
        '''Create a new window for insert the data of new suplier'''
        new_window = Toplevel()
        new_window.title("Crear nuevo proveedor")
        Label(new_window, text="Rellena el formulario y presiona Crear",font=("arial",15,"bold"), border=5).grid(row=0, column=0, columnspan=2)
        
        Label(new_window, text="Nombre: ",anchor=W).grid(row=1, column=0,)
        nombre_s = Entry(new_window,width=50)
        nombre_s.insert(0,"")
        nombre_s.grid(row=1, column=1)
        if name_buttom == "CREAR":
    
            Label(new_window, text="CIF: ", anchor=W).grid(row=2, column=0)
            cif_s = Entry(new_window,width=50)
            cif_s.insert(0,"")
            cif_s.grid(row=2, column=1)
        else:
            Label(new_window, text="CIF: ", anchor=W).grid(row=2, column=0)
            cif_s = Entry(new_window,width=50)
            cif_s.insert(0,f"{cif}")
            cif_s.grid(row=2, column=1)

        Label(new_window, text="Categoria: ").grid(row=3, column=0)
        categoria_s = Entry(new_window,width=50)
        categoria_s.insert(0,"")
        categoria_s.grid(row=3, column=1)

        Label(new_window, text="Dirección: ").grid(row=4, column=0)
        direccion_s = Entry(new_window,width=50)
        direccion_s.insert(0,"")
        direccion_s.grid(row=4, column=1)

        Label(new_window, text="Teléfono: ").grid(row=5, column=0)
        telefono_s = Entry(new_window,width=50)
        telefono_s.insert(0,"")
        telefono_s.grid(row=5, column=1)

        Label(new_window, text="Email: ").grid(row=6, column=0)
        email_s = Entry(new_window,width=50)
        email_s.insert(0,"")
        email_s.grid(row=6, column=1)

        Label(new_window, text="x1 descripción : ").grid(row=7, column=0)
        x1_descrip = Entry(new_window,width=50)
        x1_descrip.insert(0,"")
        x1_descrip.grid(row=7, column=1)

        Label(new_window, text="y1 descripción : ").grid(row=8, column=0)
        y1_descrip = Entry(new_window,width=50)
        y1_descrip.insert(0,"")
        y1_descrip.grid(row=8, column=1)

        Label(new_window, text="x2 descripción : ").grid(row=9, column=0)
        x2_descrip = Entry(new_window,width=50)
        x2_descrip.insert(0,"")
        x2_descrip.grid(row=9, column=1)

        Label(new_window, text="y2 descripción : ").grid(row=10, column=0)
        y2_descrip = Entry(new_window,width=50)
        y2_descrip.insert(0,"")
        y2_descrip.grid(row=10, column=1)

        Label(new_window, text="x1 iva : ").grid(row=11, column=0)
        x1_iva = Entry(new_window,width=50)
        x1_iva.insert(0,"")
        x1_iva.grid(row=11, column=1)

        Label(new_window, text="y1 iva : ").grid(row=12, column=0)
        y1_iva = Entry(new_window,width=50)
        y1_iva.insert(0,"")
        y1_iva.grid(row=12, column=1)

        Label(new_window, text="x2 iva : ").grid(row=13, column=0)
        x2_iva = Entry(new_window,width=50)
        x2_iva.insert(0,"")
        x2_iva.grid(row=13, column=1)

        Label(new_window, text="y2 iva : ").grid(row=14, column=0)
        y2_iva = Entry(new_window,width=50)
        y2_iva.insert(0,"")
        y2_iva.grid(row=14, column=1)

        Label(new_window, text="x1 totales : ").grid(row=15, column=0)
        x1_totales = Entry(new_window,width=50)
        x1_totales.insert(0,"")
        x1_totales.grid(row=15, column=1)

        Label(new_window, text="y1 totales : ").grid(row=16, column=0)
        y1_totales = Entry(new_window,width=50)
        y1_totales.insert(0,"")
        y1_totales.grid(row=16, column=1)

        Label(new_window, text="x2 totales : ").grid(row=17, column=0)
        x2_totales = Entry(new_window,width=50)
        x2_totales.insert(0,"")
        x2_totales.grid(row=17, column=1)

        Label(new_window, text="y2 totales : ").grid(row=18, column=0)
        y2_totales = Entry(new_window,width=50)
        y2_totales.insert(0,"")
        y2_totales.grid(row=18, column=1)
        
        Label(new_window, text="x1 precios : ").grid(row=19, column=0)
        x1_precios = Entry(new_window,width=50)
        x1_precios.insert(0,"")
        x1_precios.grid(row=19, column=1)

        Label(new_window, text="y1 precios : ").grid(row=20, column=0)
        y1_precios = Entry(new_window,width=50)
        y1_precios.insert(0,"")
        y1_precios.grid(row=20, column=1)

        Label(new_window, text="x2 precios : ").grid(row=21, column=0)
        x2_precios = Entry(new_window,width=50)
        x2_precios.insert(0,"")
        x2_precios.grid(row=21, column=1)

        Label(new_window, text="y2 precios : ").grid(row=22, column=0)
        y2_precios = Entry(new_window,width=50)
        y2_precios.insert(0,"")
        y2_precios.grid(row=22, column=1)
        
        Label(new_window, text="x1 unidades : ").grid(row=23, column=0)
        x1_unidades = Entry(new_window,width=50)
        x1_unidades.insert(0,"")
        x1_unidades.grid(row=23, column=1)

        Label(new_window, text="y1 unidades : ").grid(row=24, column=0)
        y1_unidades = Entry(new_window,width=50)
        y1_unidades.insert(0,"")
        y1_unidades.grid(row=24, column=1)

        Label(new_window, text="x2 unidades : ").grid(row=25, column=0)
        x2_unidades = Entry(new_window,width=50)
        x2_unidades.insert(0,"")
        x2_unidades.grid(row=25, column=1)

        Label(new_window, text="y2 unidades : ").grid(row=26, column=0)
        y2_unidades = Entry(new_window,width=50)
        y2_unidades.insert(0,"")
        y2_unidades.grid(row=26, column=1)
        
            
            

        if name_buttom == "CREAR":
            Button(new_window, text=f"{name_buttom}",font=("arial",15,"bold"),
                command= lambda: interface_suplier.crear_insert(new_window,win_proveedor, nombre_s.get(), cif_s.get(), categoria_s.get(),direccion_s.get(),telefono_s.get(), email_s.get(), 
                                                x1_descrip.get(),y1_descrip.get(), x2_descrip.get(), y2_descrip.get(),
                                                x1_iva.get(),y1_iva.get(),x2_iva.get(),y2_iva.get(),
                                                x1_totales.get(),y1_totales.get(),x2_totales.get(),y2_totales.get(),
                                                x1_precios.get(),y1_precios.get(),x2_precios.get(),y2_precios.get(),
                                                x1_unidades.get(),y1_unidades.get(),x2_unidades.get(),y2_unidades.get()
                                                )).grid(row=27, columnspan=2)
        else:
            Button(new_window, text=f"{name_buttom}",font=("arial",15,"bold"),
            command= lambda: interface_suplier.modify_data_suplier(new_window,win_proveedor, cif, nombre_s.get(), cif_s.get(), categoria_s.get(),direccion_s.get(),telefono_s.get(), email_s.get(), 
                                            x1_descrip.get(),y1_descrip.get(), x2_descrip.get(), y2_descrip.get(),
                                            x1_iva.get(),y1_iva.get(),x2_iva.get(),y2_iva.get(),
                                            x1_totales.get(),y1_totales.get(),x2_totales.get(),y2_totales.get(),
                                            x1_precios.get(),y1_precios.get(),x2_precios.get(),y2_precios.get(),
                                            x1_unidades.get(),y1_unidades.get(),x2_unidades.get(),y2_unidades.get()
                                            )).grid(row=27, columnspan=2)
            
            
        
    def crear_insert(new_window, win_proveedor, nombre_s, cif_s, categoria_s,direccion_s, telefono_s, email_s,
                    x1_descrip, y1_descrip, x2_descrip, y2_descrip,
                    x1_iva,y1_iva,x2_iva,y2_iva,
                    x1_totales,y1_totales,x2_totales,y2_totales,
                    x1_precios,y1_precios,x2_precios,y2_precios,
                    x1_unidades,y1_unidades,x2_unidades,y2_unidades
                    ):
        '''Create and insert data in data base'''
        
        lista_campos = [nombre_s, cif_s, categoria_s,direccion_s, telefono_s, email_s,
                    x1_descrip, y1_descrip, x2_descrip, y2_descrip,
                    x1_iva,y1_iva,x2_iva,y2_iva,
                    x1_totales,y1_totales,x2_totales,y2_totales,
                    x1_precios,y1_precios,x2_precios,y2_precios,
                    x1_unidades,y1_unidades,x2_unidades,y2_unidades]
        #if there is some empty field create a text
        [Label(new_window,text="Faltan datos por rellenar").grid(row=28,columnspan=2) for campo in lista_campos if campo == ""]
        #try:
        #Insert data
        
        db = Db()
        cif_db = db.list_cif(cif_s)
        #print("cif db:",cif_db[0])
        #print("cif_s", cif_s)
        try:
            if not cif_db[0] == cif_s:
                db.insert_tamplate_description(x1_descrip, y1_descrip, x2_descrip, y2_descrip)
                db.insert_tamplate_iva(x1_iva,y1_iva,x2_iva,y2_iva)
                
                db.insert_tamplate_totales(x1_totales,y1_totales,x2_totales,y2_totales)
                print(3)
                db.insert_tamplate_prices(x1_precios,y1_precios,x2_precios,y2_precios)
                print(4)
                sel = db.insert_tamplate_units(x1_unidades,y1_unidades,x2_unidades,y2_unidades)
                print(5)
                db.insert_suplier_db(nombre_s, cif_s, categoria_s, direccion_s, telefono_s, email_s)
                print(1)
                sel.commit()
                new_window.destroy()
                interface_suplier().limpiar_labelframe(win_proveedor)
                
                interface_suplier().proveedores_in_suplier(proveedor=win_proveedor)

            else:     
                Label(new_window,text=" Ya existe un proveedor con ese cif").grid(row=28, columnspan=2)
        except:
            db.insert_tamplate_description(x1_descrip, y1_descrip, x2_descrip, y2_descrip)
            db.insert_tamplate_iva(x1_iva,y1_iva,x2_iva,y2_iva)
            
            db.insert_tamplate_totales(x1_totales,y1_totales,x2_totales,y2_totales)
            print(3)
            db.insert_tamplate_prices(x1_precios,y1_precios,x2_precios,y2_precios)
            print(4)
            sel = db.insert_tamplate_units(x1_unidades,y1_unidades,x2_unidades,y2_unidades)
            print(5)
            db.insert_suplier_db(nombre_s, cif_s, categoria_s, direccion_s, telefono_s, email_s)
            print(1)
            sel.commit()
            new_window.destroy()
            interface_suplier().limpiar_labelframe(win_proveedor)
            
            interface_suplier().proveedores_in_suplier(proveedor=win_proveedor)
            

    def modify_data_suplier(new_window,win_proveedor,cif ,nombre_s,cif_s,categoria_s,direccion_s, telefono_s, email_s,
                    x1_descrip, y1_descrip, x2_descrip, y2_descrip,
                    x1_iva,y1_iva,x2_iva,y2_iva,
                    x1_totales,y1_totales,x2_totales,y2_totales,
                    x1_precios,y1_precios,x2_precios,y2_precios,
                    x1_unidades,y1_unidades,x2_unidades,y2_unidades
                            ):
        '''Modify some error of data in the data of suplier '''


        db = Db()
        data_of_modify = [nombre_s,cif_s,categoria_s,direccion_s, telefono_s, email_s,
                            x1_descrip, y1_descrip, x2_descrip, y2_descrip,
                            x1_iva,y1_iva,x2_iva,y2_iva,
                            x1_totales,y1_totales,x2_totales,y2_totales,
                            x1_precios,y1_precios,x2_precios,y2_precios,
                            x1_unidades,y1_unidades,x2_unidades,y2_unidades]
        print("print modifuy",data_of_modify)
        data = db.obtener_datos_plantilla(cif)
        print("data: ",data)
        for i in range(len(data_of_modify)):
            if data_of_modify[i] == "":
                data_of_modify[i] = data[i]


        print("data ya modificada: ",data_of_modify)
        
        db.update_data(cif, data_of_modify)
        new_window.destroy()
        
        

        
        
    def show_data(image, lista_plantillas: list):
        ''' Show data extracted of document'''
        img = read_and_resize(image)
        lista_articulos = get_descripcion(img,lista_plantillas[0],lista_plantillas[1],lista_plantillas[2],lista_plantillas[3])
        iva = get_iva(img,lista_articulos,lista_plantillas[4],lista_plantillas[5],lista_plantillas[6],lista_plantillas[7])
        lista_imp_total= get_precio_importe(img,lista_plantillas[8],lista_plantillas[9],lista_plantillas[10],lista_plantillas[11])
        lista_precio= get_precio_importe(img,lista_plantillas[12],lista_plantillas[13],lista_plantillas[14],lista_plantillas[15])
        units = get_units(img,lista_plantillas[16],lista_plantillas[17],lista_plantillas[18],lista_plantillas[19],lista_imp_total,lista_precio)
        print(len(lista_articulos),len(iva),len(units),len(lista_precio),len(lista_imp_total))
        df = mostrar_tablas(lista_articulos,iva, units, lista_precio, lista_imp_total)
        print(df)
        
        return df

    def proveedores_in_suplier(self, proveedor):
        import interface
        data = Db().show_all_suplier() 
        cif = StringVar()

        def select():
            select = cif.get()
            print("Cif del proveedor",select)
            return select
        
        for dato in data:
            #Create button new suplier
            Radiobutton(proveedor,pady=5,text=f"{dato['nombre']}",value= dato['cif'], variable= cif, bg="#5D6D7E").pack()
        Button(proveedor,font=("Harlow Solid",12,"bold"),cursor="hand2", text="Insertar proveedor nuevo",border=1,pady=10,bg= "#99A3A4", command= lambda: interface_suplier.new_suplier(name_buttom="CREAR", win_proveedor= proveedor, )).pack()    
        Button(proveedor,font=("Harlow Solid",12,"bold"),cursor="hand2", text="Eliminar proveedor",border=1,bg= "#99A3A4" ,pady=10, command=lambda: delete.delete_suplier(select(), proveedor)).pack()
        Button(proveedor,font=("Harlow Solid",12,"bold"),cursor="hand2", text="Modificar proveedor",border= 1,bg= "#99A3A4",pady=10, command=lambda: interface_suplier.new_suplier(cif= select(), name_buttom="ACTUALIZAR",win_proveedor=proveedor)).pack()
        Button(proveedor,font=("Harlow Solid",12,"bold"),cursor="hand2",text="Seleccionar la factura"  ,border= 1,bg= "#99A3A4" ,pady=10,command= lambda: interface.body().select_file(select(), last= True)).pack()
        return proveedor

    def limpiar_labelframe(self, label, last = False):
        '''Close and Open the app for update label frame proveedores'''
        print(last)
        print(label)
        wind = []
        if last == True:
            for widget in label.winfo_children():
                wind.append(widget)
            print(wind)
            if len(wind) >= 5:
                wind[-1].destroy()
            else:
                pass
        else:
            for widget in label.winfo_children():
                widget.destroy()







