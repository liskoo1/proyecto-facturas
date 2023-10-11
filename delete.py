import mysql.connector
from db import Db



def delete_suplier(cif, proveedor):
    import suplier
    try:
        # Connect with data base
        connect =  mysql.connector.connect(user = "root",password = "",host = "localhost", database = "tienda")
        #create cursor
        cursor = connect.cursor()
        '''Delete one suplier'''
        # Take  id_plantillas
        
        cursor.execute(f'SELECT id_plantillas FROM proveedores WHERE cif = "{cif}";')
        # get id_plantilla
        for id_plantilla in cursor:
            id_plantilla = id_plantilla
        # execute query to delete suplier
        cursor.execute(f'DELETE FROM proveedores WHERE cif = "{cif}" ;')
        cursor.execute(f'DELETE FROM plantilla_descripcion WHERE id_plantilla_des = {id_plantilla[0]} ;')
        cursor.execute(f'DELETE FROM plantilla_iva WHERE id_plantilla_iva = {id_plantilla[0]} ;')
        cursor.execute(f'DELETE FROM plantilla_precios WHERE id_plantilla_precios = {id_plantilla[0]} ;')
        cursor.execute(f'DELETE FROM plantilla_totales WHERE id_plantilla_totales = {id_plantilla[0]} ;')
        cursor.execute(f'DELETE FROM plantilla_unidades WHERE id_plantilla_unidades = {id_plantilla[0]} ;')
        # Make commit 
        connect.commit()
        db= Db()
        data = db.show_all_suplier()
        #clean the suplier delete
        suplier.interface_suplier().limpiar_labelframe(label=proveedor)
        # and regenerate buttons and label
        suplier.interface_suplier().proveedores_in_suplier(proveedor)
        return data
    except:
        print("No a sido posible borrar el proveedor")

    