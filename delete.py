import mysql.connector
from db import Db



def delete_suplier(cif, proveedor):
    import suplier
    try:
        connect =  mysql.connector.connect(user = "root",password = "ktmexc200",host = "localhost", database = "tienda")

        cursor = connect.cursor()
        '''Delete one suplier'''
        # Take  id_plantillas
        print("esto es cif", cif)
        cursor.execute(f'SELECT id_plantillas FROM proveedores WHERE cif = "{cif}";')

        for id_plantilla in cursor:
            id_plantilla = id_plantilla
        print(id_plantilla[0])
        cursor.execute(f'DELETE FROM proveedores WHERE cif = "{cif}" ;')
        cursor.execute(f'DELETE FROM plantilla_descripcion WHERE id_plantilla_des = {id_plantilla[0]} ;')
        cursor.execute(f'DELETE FROM plantilla_iva WHERE id_plantilla_iva = {id_plantilla[0]} ;')
        cursor.execute(f'DELETE FROM plantilla_precios WHERE id_plantilla_precios = {id_plantilla[0]} ;')
        cursor.execute(f'DELETE FROM plantilla_totales WHERE id_plantilla_totales = {id_plantilla[0]} ;')
        cursor.execute(f'DELETE FROM plantilla_unidades WHERE id_plantilla_unidades = {id_plantilla[0]} ;')
        connect.commit()
        db= Db()
        data = db.show_all_suplier()
        suplier.interface_suplier().limpiar_labelframe(label=proveedor)

        suplier.interface_suplier().proveedores_in_suplier(proveedor)
        
        
        # Make commit 
        
        return data
    except:
        print("No a sido posible borrar el proveedor")

    