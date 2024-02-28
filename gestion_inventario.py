import pickle

class Articulo:
    def __init__(self, codigo, titulo, stock, costo):
        self.codigo = codigo
        self.titulo = titulo
        self.stock = stock
        self.costo = costo

    def __repr__(self):
        return f"Código: {self.codigo}, Título: {self.titulo}, Stock: {self.stock}, Costo: {self.costo}"

class Almacen:
    def __init__(self):
        self.articulos = {}

    def anadir_articulo(self, articulo):
        self.articulos[articulo.codigo] = articulo
        print("Artículo añadido con éxito.")

    def remover_articulo(self, codigo):
        if codigo in self.articulos:
            del self.articulos[codigo]
            print("Artículo removido con éxito.")
        else:
            print("Ese artículo no existe en el inventario.")

    def modificar_articulo(self, codigo, stock=None, costo=None):
        if codigo in self.articulos:
            if stock is not None:
                self.articulos[codigo].stock = stock
            if costo is not None:
                self.articulos[codigo].costo = costo
            print("Artículo modificado con éxito.")
        else:
            print("No se encontró el artículo solicitado.")

    def localizar_articulo(self, titulo):
        encontrado = False
        for articulo in self.articulos.values():
            if titulo.lower() in articulo.titulo.lower():
                print(articulo)
                encontrado = True
        if not encontrado:
            print("Artículo no localizado.")

    def listar_articulos(self):
        for articulo in self.articulos.values():
            print(articulo)

    def persistir_almacen(self, archivo='almacen.pkl'):
        with open(archivo, 'wb') as archivo_salida:
            pickle.dump(self.articulos, archivo_salida)

    def recuperar_almacen(self, archivo='almacen.pkl'):
        try:
            with open(archivo, 'rb') as archivo_entrada:
                self.articulos = pickle.load(archivo_entrada)
        except FileNotFoundError:
            print("Archivo del almacén no encontrado, se iniciará un almacén nuevo.")

def interfaz_usuario():
    almacen = Almacen()
    almacen.recuperar_almacen()

    while True:
        print("\n1. Añadir artículo\n2. Remover artículo\n3. Modificar artículo\n4. Localizar artículo\n5. Listar artículos\n6. Guardar y cerrar sesión")
        eleccion = input("Elija una opción: ")
        
        if eleccion == '1':
            codigo = input("Código del artículo: ")
            titulo = input("Título del artículo: ")
            stock = int(input("Stock del artículo: "))
            costo = float(input("Costo del artículo: "))
            almacen.anadir_articulo(Articulo(codigo, titulo, stock, costo))
            
        elif eleccion == '2':
            codigo = input("Código del artículo a remover: ")
            almacen.remover_articulo(codigo)
            
        elif eleccion == '3':
            codigo = input("Código del artículo a modificar: ")
            stock = input("Nuevo stock (presiona enter para no cambiar): ")
            costo = input("Nuevo costo (presiona enter para no cambiar): ")
            stock = int(stock) if stock else None
            costo = float(costo) if costo else None
            almacen.modificar_articulo(codigo, stock, costo)
            
        elif eleccion == '4':
            titulo = input("Título del artículo a localizar: ")
            almacen.localizar_articulo(titulo)
            
        elif eleccion == '5':
            almacen.listar_articulos()
            
        elif eleccion == '6':
            almacen.persistir_almacen()
            print("Almacén guardado con éxito. Finalizando sesión.")
            break
        else:
            print("Ha seleccionado una opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    interfaz_usuario()
