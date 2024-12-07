"""
Correccion Profesor es lo que tiene #
"""
"""
Creo diccionarios de La tienda de frutas
"""
TiendaFruta={"Manzana": {"Precio" : 1.2, "Stock": 50,"Proveedores" : ("ProveedorA","ProveedorB")},
             "Naranja" : {"Precio" : 0.8, "Stock": 80,"Proveedores" : ("ProveedorC","ProveedorD")}}
 
"""
Modifico Precio de la Manzana
"""
TiendaFruta["Manzana"]["Precio"] = 1.5
# print(TiendaFruta["Manzana"]["Precio"])
"""
Aumenta el Stock Naranjas
"""

TiendaFruta["Naranja"]["Stock"] = TiendaFruta["Naranja"]["Stock"]+20
# print(TiendaFruta["Naranja"]["Stock"])

"""
Elimino ProveedorB
"""
del TiendaFruta["Manzana"]["Proveedores"]
TiendaFruta["Manzana"]["Proveedores"]= ("ProveedorA",)
# print(TiendaFruta["Manzana"]["Proveedores"])

"""
Consulta precio Naranja
"""
print(TiendaFruta["Naranja"]["Precio"])

"""
Convertir tupla en lista
"""
TiendaFruta["Naranja"]["Proveedores"] = list(TiendaFruta["Naranja"]["Proveedores"])
TiendaFruta["Naranja"]["Proveedores"][0]="ProveedorE"
# print(TiendaFruta["Naranja"]["Proveedores"])

"""
Consulta N Proveedores Manzana
"""
print(len(TiendaFruta["Manzana"]["Proveedores"]))

"""
Añadimos Platano
"""
TiendaFruta["Platano"]= {"Precio" : 0.9, "Stock": 120,"Proveedores" : ("ProveedorF","ProveedorG")}
# print(TiendaFruta["Platano"])
"""
Añandimos Descuentos
"""
TiendaFruta["Manzana"]["Descuento"]= 0.10
TiendaFruta["Naranja"]["Descuento"]= 0.05
TiendaFruta["Platano"]["Descuento"]= 0.15
# print(TiendaFruta)
"""
Precio Descuento
"""
Precio= TiendaFruta["Manzana"]["Precio"]*5*(1-TiendaFruta["Manzana"]["Descuento"])
print(Precio)
TiendaFruta["Manzana"]["Stock"]=TiendaFruta["Manzana"]["Stock"]-5

"""
Numero Total de Frutas
"""
FrutasTotales= TiendaFruta["Manzana"]["Stock"]+TiendaFruta["Naranja"]["Stock"]+TiendaFruta["Platano"]["Stock"]
print(FrutasTotales)
