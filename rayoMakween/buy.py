    
class Carrito:
    def __init__(self,request):
        self.request = request
        self.session =request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito 
        
    #CREA UN OBJETO producto CRUD
    def agregar(self, producto):
        if producto.codigo not in self.carrito.keys():
            self.carrito[producto.codigo]={
                'id_producto' : producto.codigo,
                'marca' : producto.marca,
                'modelo': producto.nombre,
                'precio' : str(producto.precio),
                'cantidad' : 1,
                'total' : producto.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key == producto.codigo:
                    value['cantidad'] = value['cantidad']+1
                    value['precio'] = producto.precio
                    value['total'] = value['total'] + producto.precio,
                    break
        self.guardar_carrito()
    
    #GUARDA UN producto CRUD
    def guardar_carrito(self):
        self.session['carrito'] = self.guardar_carrito
        self.session.modified = True

    #ELIMINA UN producto CRUD
    def eliminar(self, producto):
        id= producto.codigo
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    #ELIMINA LA CANTIDAD, EL VALOR DEL producto SEGUN EL KEYS Y ELIMINA EL producto -- ELIMINA EL producto ELEGIDO SEGUN PATENTE
    def restar (self, producto):
        for key, value in self.carrito.items():
            if key == producto.codigo:
                value['cantidad'] = value['cantidad']-1
                value['total'] = int(value['total'])-producto.precio
                if value['cantidad']<1:
                    self.eliminar(producto)
                break
        self.guardar_carrito()

    #LIMPIA EL INGRESO
    def limpiar(self):
        self.session['carrito']={}
        self.session.modified= True 

    

