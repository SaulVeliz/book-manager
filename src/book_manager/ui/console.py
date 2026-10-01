from book_manager.entities.entities import Libro
from book_manager.entities.entities import Genero
from book_manager.entities.entities import Editorial
from book_manager.entities.entities import Moneda
from book_manager.entities.entities import Precio
from book_manager.entities.entities import TipoCotizacion
from book_manager.entities.entities import Stock
from book_manager.entities.entities import CotizacionDolar
from datetime import date
from book_manager.preload_data.csv_data import (
    guardar_genero,
    guardar_todos_los_generos,
    cargar_generos,
    guardar_todas_las_editoriales,
    guardar_todas_las_monedas,
    guardar_todos_los_libros,
    guardar_todos_los_precios
    )


class ConsoleUI:

    def __init__(
        self,
        libro_service,
        genero_service,
        editorial_service,
        moneda_service,
        precio_service,
        tipo_service,
        stock_service,
        cotizacion_service
    ):
        self.libro_service = libro_service
        self.genero_service = genero_service
        self.editorial_service = editorial_service
        self.moneda_service = moneda_service
        self.precio_service = precio_service      
        self.tipo_service = tipo_service
        self.stock_service = stock_service
        self.cotizacion_service = cotizacion_service


    def mostrar_menu(self):

        while True:

            print("\n" + "=" * 40)
            print("       BOOK MANAGER")
            print("=" * 40)

            print("1. Libros")
            print("2. Géneros")
            print("3. Editoriales")
            print("4. Monedas")
            print("5. Precios")
            print("6. Tipos de Cotizacion")
            print("7. Stock")
            print("8. Cotizaciones dolar")
            print("0. Salir")

            opcion = input(
                "\nSeleccione una opción: "
            )

            if opcion == "1":
                self.menu_libros()

            elif opcion == "2":
                self.menu_generos()

            elif opcion == "3":
                self.menu_editoriales()

            elif opcion == "4":
                self.menu_monedas()

            elif opcion == "5":
                self.menu_precios()

            elif opcion == "6":
                self.menu_tipos_cotizacion()

            elif opcion == "7":
                self.menu_stock()

            elif opcion == "8":
                self.menu_cotizaciones()

            elif opcion == "0":
                print("\nSaliendo...")
                break

            else:
                print("\nOpción inválida")
                


    def listar_libros(self):
        print("\n=== LIBROS ===\n")
        print("********************")
        for libro in self.libro_service.listar():
            print(libro)



    def listar_generos(self):
        print("\n=== GENEROS ===\n")
        print("********************")
        for genero in self.genero_service.listar():
            print(genero)



    def listar_editoriales(self):
        print("\n=== EDITORIALES ===\n")
        print("********************")
        for editorial in self.editorial_service.listar():
            print(editorial)



    def listar_monedas(self):
        print("\n=== MONEDAS ===\n")
        print("********************")
        for moneda in self.moneda_service.listar():
            print(moneda)


    def listar_precio(self):
        print("\n=== PRECIOS ===\n")
        print("********************")
        for precio in self.precio_service.listar():
            print(precio)


    def listar_tipos_cotizacion(self):
        print("\n=== TIPOS DE COTIZACION ===\n")
        print("********************")
        for tipo in self.tipo_service.listar():
            print(tipo)


    def listar_stock(self):

        print("\n=== STOCK ===\n")
        print("********************")

        for stock in self.stock_service._stock_repo._datos.values():
            print(stock)


    def listar_cotizaciones(self):

        print("\n=== COTIZACIONES ===\n")
        print("********************")

        for cotizacion in (
            self.cotizacion_service
            ._cotizacion_repo
            ._datos
            .values()
        ):
            print(cotizacion)


#**************************************************************************
#Menu con opciones de la seccion libros

    def menu_libros(self):

        while True:
            print("\n    LIBROS    ")
            print("********************")

            print("1. Listar")
            print("2. Agregar")
            print("3. Modificar")
            print("4. Eliminar")
            print("5. Ver detalle")
            print("0. Volver")

            opcion = input("\nOpcion: ")

            if opcion == "1":
                self.listar_libros()

            elif opcion == "2":
                self.agregar_libro()

            elif opcion == "3":
                self.modificar_libro()

            elif opcion == "4":
                self.eliminar_libro()

            elif opcion == "5":
                self.detalle_libro()

            elif opcion == "0":
                break

            else:
                print("Opcion invalida")


#Seccion CRUD Libros

    def agregar_libro(self):

        try:
            id_ = int(input("ID: "))
            isbn = input("ISBN: ")
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            genero_id = int(input("Genero ID: "))
            editorial_id = int(input("Editorial ID: "))

            libro = Libro(
                id=id_,
                isbn=isbn,
                titulo=titulo,
                autor=autor,
                genero_id=genero_id,
                editorial_id=editorial_id
            )

            self.libro_service.crear(libro)
            guardar_todos_los_libros(
                self.libro_service.listar()
            )

            print("\nLibro agregado correctamente")

        except Exception as e:
            print(f"\nError: {e}")
            

    def modificar_libro(self):

        try:

            id_ = int(input("ID del libro a modificar: "))

            libro = self.libro_service.obtener_por_id(id_)

            if libro is None:
                print("\nLibro no encontrado")
                return
            
            isbn = input(f"ISBN [{libro.isbn}]: ")
            titulo = input(f"Título [{libro.titulo}]: ")
            autor = input(f"Autor [{libro.autor}]: ")
            genero_id = input(f"Género ID [{libro.genero_id}]: ")
            editorial_id = input(f"Editorial ID [{libro.editorial_id}]: ")

            if isbn:
                libro.isbn = isbn

            if titulo:
                libro.titulo = titulo

            if autor:
                libro.autor = autor

            if genero_id:
                libro.genero_id = int(genero_id)

            if editorial_id:
                libro.editorial_id = int(editorial_id)

            self.libro_service.actualizar(libro)

            guardar_todos_los_libros(
            self.libro_service.listar()
            )

            print("\nLibro actualizado correctamente")

        except Exception as e:
            print(f"\nError: {e}")
        

    def eliminar_libro(self):

        try:

            id_ = int(
                input("ID del libro a eliminar: ")
            )

            eliminado = (
                self.libro_service.eliminar(id_)
            )

            guardar_todos_los_libros(
            self.libro_service.listar()
            )

            if eliminado:
                print("Libro eliminado")
            else:
                print("Libro inexistente")

        except Exception as e:
            print(f"Error: {e}")

    def detalle_libro(self):

        try:

            id_ = int(
                input("ID del libro: ")
            )

            libro = (
                self.libro_service.obtener_por_id(
                    id_
                )
            )

            if libro is None:

                print(
                    "\nLibro no encontrado"
                )

                return

            genero = (
                self.genero_service.obtener_por_id(
                    libro.genero_id
                )
            )

            editorial = (
                self.editorial_service.obtener_por_id(
                    libro.editorial_id
                )
            )

            print("\n=== DETALLE LIBRO ===")
            print("************************")

            print(
                f"\nTitulo: {libro.titulo}"
            )

            print(
                f"ISBN: {libro.isbn}"
            )

            print(
                f"Autor: {libro.autor}"
            )

            if genero:
                print(
                    f"Genero: {genero.nombre}"
                )

            if editorial:
                print(
                    f"Editorial: {editorial.nombre}"
                )

            precio_encontrado = None

            for precio in self.precio_service.listar():

                if precio.libro_id == libro.id:

                    precio_encontrado = precio
                    break

            if precio_encontrado:

                moneda = (
                    self.moneda_service.obtener_por_id(
                        precio_encontrado.moneda_id
                    )
                )

                simbolo = ""

                if moneda:
                    simbolo = moneda.simbolo

                codigo_moneda = ""

                if moneda:
                    codigo_moneda = moneda.codigo

                print(
                    f"Precio: {simbolo}{precio_encontrado.valor} {codigo_moneda}"
                )

        except Exception as e:
            print(
                f"\nError: {e}"
            )


#**************************************************************************
#Menu con opciones de la seccion generos

    def menu_generos(self):

        while True:

            print("\n=== GENEROS ===")
            print("********************")

            print("1. Listar")
            print("2. Agregar")
            print("3. Modificar")
            print("4. Eliminar")
            print("0. Volver")

            opcion = input("\nOpcion: ")

            if opcion == "1":
                self.listar_generos()

            elif opcion == "2":
                self.agregar_genero()

            elif opcion == "3":
                self.modificar_genero()

            elif opcion == "4":
                self.eliminar_genero()

            elif opcion == "0":
                break

            else:
                print("Opcion invalida")


#Seccion CRUD Genero

    from book_manager.preload_data.csv_data import (
        guardar_genero
)

    from book_manager.preload_data.csv_data import (
    guardar_genero
)

    def agregar_genero(self):

        try:

            id_ = int(input("ID: "))
            nombre = input("Nombre: ")
            descripcion = input("Descripcion: ")

            genero = Genero(
                id=id_,
                nombre=nombre,
                descripcion=descripcion
            )

            self.genero_service.crear(genero)

            guardar_genero(
                genero.id,
                genero.nombre,
                genero.descripcion
            )

            print("\nGenero agregado correctamente")

        except Exception as e:
            print(f"\nError: {e}")


    def modificar_genero(self):

            try:

                id_ = int(
                    input("ID del genero a modificar: ")
                )

                genero = (
                    self.genero_service.obtener_por_id(id_)
                )

                if genero is None:
                    print("\nGenero no encontrado")
                    return

                nombre = input(
                    f"Nombre [{genero.nombre}]: "
                )

                descripcion = input(
                    f"Descripcion [{genero.descripcion}]: "
                )

                if nombre:
                    genero.nombre = nombre

                if descripcion:
                    genero.descripcion = descripcion

                self.genero_service.actualizar(
                    genero
                )

                guardar_todos_los_generos(
                self.genero_service.listar()
                )

                print(
                    "\nGenero actualizado correctamente"
                )

            except Exception as e:
                print(f"\nError: {e}")


    def eliminar_genero(self):
    
            try:
    
                id_ = int(
                    input("ID del genero a eliminar: ")
                )
    
                genero = (
                    self.genero_service.eliminar(id_)
                )
    
                if genero:
                     guardar_todos_los_generos(
                        self.genero_service.listar()
                )
                     
                print("Genero eliminado")
    
            except Exception as e:
                print(f"Error: {e}")
            

#**************************************************************************
#Menu con opciones de la seccion editoriales

    def menu_editoriales(self):

        while True:

            print("\n=== EDITORIALES ===")
            print("********************")

            print("1. Listar")
            print("2. Agregar")
            print("3. Modificar")
            print("4. Eliminar")
            print("0. Volver")

            opcion = input("\nOpcion: ")

            if opcion == "1":
                self.listar_editoriales()

            elif opcion == "2":
                self.agregar_editorial()

            elif opcion == "3":
                self.modificar_editorial()

            elif opcion == "4":
                self.eliminar_editorial()

            elif opcion == "0":
                break

            else:
                print("Opcion invalida")


#Seccion CRUD Editoriales

    def agregar_editorial(self):

        try:

            id_ = int(input("ID: "))
            nombre = input("Nombre: ")
            pais = input("Pais: ")

            editorial = Editorial(
                id=id_,
                nombre=nombre,
                pais=pais
            )

            self.editorial_service.crear(editorial)
            guardar_todas_las_editoriales(
                self.editorial_service.listar()
            )           

            print("\nEditorial agregado correctamente")

        except Exception as e:
            print(f"\nError: {e}")


    def modificar_editorial(self):

        try:

            id_ = int(
                input("ID del editorial a modificar: ")
            )

            editorial = (
                self.editorial_service.obtener_por_id(id_)
            )

            if editorial is None:
                print("\nEditorial no encontrado")
                return

            nombre = input(
                f"Nombre [{editorial.nombre}]: "
            )

            pais = input(
                f"Pais [{editorial.pais}]: "
            )

            if nombre:
                editorial.nombre = nombre

            if pais:
                editorial.pais = pais

            self.editorial_service.actualizar(
                editorial
            )

            guardar_todas_las_editoriales(
                self.editorial_service.listar()
            )

            print(
                "\nEditorial actualizado correctamente"
            )

        except Exception as e:
            print(f"\nError: {e}")


    def eliminar_editorial(self):
    
            try:
    
                id_ = int(
                    input("ID del editorial a eliminar: ")
                )
    
                eliminado = (
                    self.editorial_service.eliminar(id_)
                )

                guardar_todas_las_editoriales(
                    self.editorial_service.listar()
                )
    
                if eliminado:
                    print("Editorial eliminado")
                else:
                    print("Editorial inexistente")
    
            except Exception as e:
                print(f"Error: {e}")


#**************************************************************************
#Menu con opciones de la seccion monedas

    def menu_monedas(self):

        while True:

            print("\n=== MONEDAS ===")
            print("********************")

            print("1. Listar")
            print("2. Agregar")
            print("3. Modificar")
            print("4. Eliminar")
            print("0. Volver")

            opcion = input("\nOpcion: ")

            if opcion == "1":
                self.listar_monedas()

            elif opcion == "2":
                self.agregar_moneda()

            elif opcion == "3":
                self.modificar_moneda()

            elif opcion == "4":
                self.eliminar_moneda()

            elif opcion == "0":
                break

            else:
                print("Opcion invalida")


#Seccion CRUD Monedas

    def agregar_moneda(self):

            try:

                id = int(input("ID: "))
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                simbolo = input("Simbolo: ")

                moneda = Moneda(
                    id,
                    codigo,
                    nombre,
                    simbolo
                )

                self.moneda_service.crear(moneda)

                guardar_todas_las_monedas(
                    self.moneda_service.listar()
                )

                print("\nMoneda agregado correctamente")

            except Exception as e:
                print(f"\nError: {e}")


   
    def modificar_moneda(self):

            try:

                id_ = int(
                    input("ID de la moneda a modificar: ")
                )

                moneda = (
                    self.moneda_service.obtener_por_id(id_)
                )

                if moneda is None:
                    print("\nMoneda no encontrado")
                    return

                codigo = input(
                    f"Codigo [{moneda.codigo}]: "
                )

                nombre = input(
                    f"Nombre [{moneda.nombre}]: "
                )

                simbolo = input(
                    f"Simbolo [{moneda.simbolo}]: "
                )

                if nombre:
                    moneda.codigo = codigo

                if nombre:
                    moneda.nombre = nombre

                if nombre:
                    moneda.simbolo = simbolo

                self.moneda_service.actualizar(
                    moneda
                )

                print(
                    "\nMoneda actualizada correctamente"
                )

            except Exception as e:
                print(f"\nError: {e}")


    def eliminar_moneda(self):
        
                try:
        
                    id_ = int(
                        input("ID de la moneda a eliminar: ")
                    )
        
                    eliminado = (
                        self.moneda_service.eliminar(id_)
                    )
        
                    if eliminado:
                        print("Moneda eliminada")
                    else:
                        print("Moneda inexistente")
        
                except Exception as e:
                    print(f"Error: {e}")

#**************************************************************************
#Menu con opciones de la seccion precios

    def menu_precios(self):

        while True:

            print("\n=== PRECIOS ===")
            print("********************")

            print("1. Listar")
            print("2. Agregar")
            print("3. Modificar")
            print("4. Eliminar")
            print("0. Volver")

            opcion = input("\nOpcion: ")

            if opcion == "1":
                self.listar_precio()

            elif opcion == "2":
                self.agregar_precio()

            elif opcion == "3":
                self.modificar_precio()

            elif opcion == "4":
                self.eliminar_precio()

            elif opcion == "0":
                break

            else:
                print("Opcion invalida")


#Seccion CRUD Precios

    def agregar_precio(self):

        try:

            id_ = int(input("ID: "))
            libro_id = int(input("Libro ID: "))
            moneda_id = int(input("Moneda ID: "))
            valor = float(input("Valor: "))

            precio = Precio(
                id=id_,
                libro_id=libro_id,
                moneda_id=moneda_id,
                valor=valor
            )

            self.precio_service.crear(precio)
            guardar_todos_los_precios(
            self.precio_service.listar()
            )


            print("\nPrecio agregado correctamente")

        except Exception as e:
            print(f"\nError: {e}")


    def modificar_precio(self):

        try:

            id_ = int(
                input("ID del precio a modificar: ")
            )

            precio = (
                self.precio_service.obtener_por_id(id_)
            )

            if precio is None:
                print("\nPrecio no encontrado")
                return

            libro_id = input(
                f"Libro ID [{precio.libro_id}]: "
            )

            moneda_id = input(
                f"Moneda ID [{precio.moneda_id}]: "
            )

            valor = input(
                f"Valor [{precio.valor}]: "
            )

            if libro_id:
                precio.libro_id = int(libro_id)

            if moneda_id:
                precio.moneda_id = int(moneda_id)

            if valor:
                precio.valor = float(valor)

            self.precio_service.actualizar(
                precio
            )
            guardar_todos_los_precios(
            self.precio_service.listar()
            )

            print(
                "\nPrecio actualizado correctamente"
            )

        except Exception as e:
            print(f"\nError: {e}")
    

    def eliminar_precio(self):

        try:

            id_ = int(
                input("ID del precio a eliminar: ")
            )

            eliminado = (
                self.precio_service.eliminar(id_)
            )
            guardar_todos_los_precios(
            self.precio_service.listar()
            )

            if eliminado:
                print("\nPrecio eliminado")
            else:
                print("\nPrecio inexistente")

        except Exception as e:
            print(f"\nError: {e}")



#**************************************************************************
#Menu con opciones de la seccion tipo de cotizaciones

    def menu_tipos_cotizacion(self):

        while True:

            print("\n=== TIPOS DE COTIZACION ===")
            print("******************************")

            print("1. Listar")
            print("2. Agregar")
            print("3. Modificar")
            print("4. Eliminar")
            print("0. Volver")

            opcion = input("\nOpcion: ")

            if opcion == "1":
                self.listar_tipos_cotizacion()

            elif opcion == "2":
                self.agregar_tipo_cotizacion()

            elif opcion == "3":
                self.modificar_tipo_cotizacion()

            elif opcion == "4":
                self.eliminar_tipo_cotizacion()

            elif opcion == "0":
                break

            else:
                print("Opcion invalida")

#Seccion CRUD Tipo de Cotizacion

    def agregar_tipo_cotizacion(self):

        try:

            id_ = int(input("ID: "))
            nombre = input("Nombre: ")

            tipo = TipoCotizacion(
                id=id_,
                nombre=nombre
            )

            self.tipo_service.crear(tipo)

            print(
                "\nTipo de cotizacion agregado correctamente"
            )

        except Exception as e:
            print(f"\nError: {e}")


    def modificar_tipo_cotizacion(self):

        try:

            id_ = int(
                input(
                    "ID del tipo de cotizacion a modificar: "
                )
            )

            tipo = (
                self.tipo_service.obtener_por_id(id_)
            )

            if tipo is None:
                print(
                    "\nTipo de cotizacion no encontrado"
                )
                return

            nombre = input(
                f"Nombre [{tipo.nombre}]: "
            )

            if nombre:
                tipo.nombre = nombre

            self.tipo_service.actualizar(tipo)

            print(
                "\nTipo de cotizacion actualizado"
            )

        except Exception as e:
            print(f"\nError: {e}")


    def eliminar_tipo_cotizacion(self):

        try:

            id_ = int(
                input(
                    "ID del tipo de cotizacion a eliminar: "
                )
            )

            eliminado = (
                self.tipo_service.eliminar(id_)
            )

            if eliminado:
                print(
                    "\nTipo de cotizacion eliminado"
                )
            else:
                print(
                    "\nTipo de cotizacion inexistente"
                )

        except Exception as e:
            print(f"\nError: {e}")



#**************************************************************************
#Menu con opciones de la seccion stock

    def menu_stock(self):

        while True:

            print("\n=== STOCK ===")
            print("********************")

            print("1. Listar")
            print("2. Agregar")
            print("3. Modificar")
            print("4. Eliminar")
            print("0. Volver")

            opcion = input("\nOpcion: ")

            if opcion == "1":
                self.listar_stock()

            elif opcion == "2":
                self.agregar_stock()

            elif opcion == "3":
                self.modificar_stock()

            elif opcion == "4":
                self.eliminar_stock()

            elif opcion == "0":
                break

            else:
                print("Opcion invalida")


#Seccion CRUD Stock

    def agregar_stock(self):

        try:

            libro_id = int(input("Libro ID: "))
            cantidad = int(input("Cantidad: "))

            stock = Stock(
                libro_id=libro_id,
                cantidad=cantidad
            )

            self.stock_service.crear(stock)

            print("\nStock agregado correctamente")

        except Exception as e:
            print(f"\nError: {e}")


    def modificar_stock(self):

        try:

            libro_id = int(
                input("Libro ID del stock: ")
            )

            stock = (
                self.stock_service.obtener_por_libro(
                    libro_id
                )
            )

            if stock is None:
                print("\nStock no encontrado")
                return

            cantidad = input(
                f"Cantidad [{stock.cantidad}]: "
            )

            if cantidad:
                stock.cantidad = int(cantidad)

            self.stock_service.actualizar(stock)

            print(
                "\nStock actualizado correctamente"
            )

        except Exception as e:
            print(f"\nError: {e}")


    def eliminar_stock(self):

        try:

            libro_id = int(
                input("Libro ID a eliminar: ")
            )

            eliminado = (
                self.stock_service.eliminar(libro_id)
            )

            if eliminado:
                print("\nStock eliminado")
            else:
                print("\nStock inexistente")

        except Exception as e:
            print(f"\nError: {e}")



#**************************************************************************
#Menu con opciones de la seccion cotizacion

    def menu_cotizaciones(self):

        while True:

            print("\n=== COTIZACIONES DOLAR ===")
            print("*****************************")

            print("1. Listar")
            print("2. Agregar")
            print("3. Modificar")
            print("4. Eliminar")
            print("0. Volver")

            opcion = input("\nOpcion: ")

            if opcion == "1":
                self.listar_cotizaciones()

            elif opcion == "2":
                self.agregar_cotizacion()

            elif opcion == "3":
                self.modificar_cotizacion()

            elif opcion == "4":
                self.eliminar_cotizacion()

            elif opcion == "0":
                break

            else:
                print("Opcion invalida")

#Seccion CRUD Cotizaciones

    def agregar_cotizacion(self):

        try:

            tipo_id = int(input("Tipo ID: "))

            fecha_texto = input(
                "Fecha (AAAA-MM-DD): "
            )

            valor = float(input("Valor: "))

            fecha = date.fromisoformat(
                fecha_texto
            )

            cotizacion = CotizacionDolar(
                tipo_id=tipo_id,
                fecha=fecha,
                valor=valor
            )

            self.cotizacion_service.crear(
                cotizacion
            )

            print(
                "\nCotizacion agregada correctamente"
            )

        except Exception as e:
            print(f"\nError: {e}")


    def modificar_cotizacion(self):

        try:

            tipo_id = int(
                input("Tipo ID: ")
            )

            fecha_texto = input(
                "Fecha (AAAA-MM-DD): "
            )

            fecha = date.fromisoformat(
                fecha_texto
            )

            cotizacion = (
                self.cotizacion_service.obtener(
                    tipo_id,
                    fecha
                )
            )

            if cotizacion is None:

                print(
                    "\nCotizacion no encontrada"
                )

                return

            valor = input(
                f"Valor [{cotizacion.valor}]: "
            )

            if valor:
                cotizacion.valor = float(
                    valor
                )

            self.cotizacion_service.actualizar(
                cotizacion
            )

            print(
                "\nCotizacion actualizada"
            )

        except Exception as e:
            print(f"\nError: {e}")


    def eliminar_cotizacion(self):

        try:

            tipo_id = int(
                input("Tipo ID: ")
            )

            fecha_texto = input(
                "Fecha (AAAA-MM-DD): "
            )

            fecha = date.fromisoformat(
                fecha_texto
            )

            eliminado = (
                self.cotizacion_service.eliminar(
                    tipo_id,
                    fecha
                )
            )

            if eliminado:

                print(
                    "\nCotizacion eliminada"
                )

            else:

                print(
                    "\nCotizacion inexistente"
                )

        except Exception as e:
            print(f"\nError: {e}")
