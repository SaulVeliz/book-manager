from book_manager.database.connection import ConexionDB
from book_manager.models.models import GeneroModel
from book_manager.database.connection import ConexionDB
from book_manager.models.models import (
    GeneroModel,
    EditorialModel,
    MonedaModel,
    LibroModel,
    PrecioModel,
    TipoCotizacionModel,
    StockModel,
    CotizacionDolarModel
)


class GeneroRepositorySQL:

    def __init__(self):
        self.db = ConexionDB()

    def leer_todos(self):
        with self.db.get_session() as session:
            return session.query(
                GeneroModel
            ).all()
        
    def leer_por_id(self,id_: int):
        with self.db.get_session() as session:
            return session.get(
                GeneroModel,
                id_
            )

    def crear(self,genero):
        genero_model = GeneroModel(
            id=genero.id,
            nombre=genero.nombre,
            descripcion=genero.descripcion
        )

        with self.db.get_session() as session:
            session.add(genero_model)

            return genero_model

    def actualizar(self,genero):

        with self.db.get_session() as session:
            genero_model = session.get(
                GeneroModel,
                genero.id
            )
            if genero_model:

                genero_model.nombre = genero.nombre
                genero_model.descripcion = genero.descripcion

            return genero_model

    def eliminar(self,id_: int):
        with self.db.get_session() as session:
            genero_model = session.get(
                GeneroModel,
                id_
            )
            if not genero_model:
                return False

            session.delete(genero_model)

            return True


class EditorialRepositorySQL:

    def __init__(self):
        self.db = ConexionDB()

    def leer_todos(self):
        with self.db.get_session() as session:
            return session.query(
                EditorialModel
            ).all()

    def leer_por_id(self,id_: int):
        with self.db.get_session() as session:
            return session.get(
                EditorialModel,
                id_
            )

    def crear(self,editorial):

        editorial_model = EditorialModel(
            id=editorial.id,
            nombre=editorial.nombre,
            pais=editorial.pais
        )
        with self.db.get_session() as session:
            session.add(editorial_model)
            return editorial_model

    def actualizar(self,editorial):

        with self.db.get_session() as session:
            editorial_model = session.get(
                EditorialModel,
                editorial.id
            )
            if editorial_model:

                editorial_model.nombre = editorial.nombre
                editorial_model.pais = editorial.pais

            return editorial_model

    def eliminar(self,id_: int):
        with self.db.get_session() as session:
            editorial_model = session.get(
                EditorialModel,
                id_
            )

            if not editorial_model:
                return False

            session.delete(editorial_model)

            return True


class MonedaRepositorySQL:

    def __init__(self):
        self.db = ConexionDB()

    def leer_todos(self):    
            with self.db.get_session() as session:    
                return session.query(
                    MonedaModel
                ).all()

    def leer_por_id(self,id_: int):
        with self.db.get_session() as session:

            return session.get(
                MonedaModel,
                id_
            )
        
    def crear(self,moneda):

        moneda_model = MonedaModel(
            id=moneda.id,
            codigo=moneda.codigo,
            nombre=moneda.nombre,
            simbolo=moneda.simbolo
        )
        with self.db.get_session() as session:
            session.add(moneda_model)
            return moneda_model

    def actualizar(self,moneda):

        with self.db.get_session() as session:
            moneda_model = session.get(
                MonedaModel,
                moneda.id
            )
            if moneda_model:

                moneda_model.codigo = moneda.codigo
                moneda_model.nombre = moneda.nombre
                moneda_model.simbolo = moneda.simbolo

            return moneda_model

    def eliminar(self,id_: int):

        with self.db.get_session() as session:
            moneda_model = session.get(
                MonedaModel,
                id_
            )

            if not moneda_model:
                return False

            session.delete(moneda_model)

            return True
        

class LibroRepositorySQL:

    def __init__(self):
        self.db = ConexionDB()

    def leer_todos(self):
        with self.db.get_session() as session:
            return session.query(
                LibroModel
            ).all()

    def leer_por_id(self, id_: int):

        with self.db.get_session() as session:

            return session.get(
                LibroModel,
                id_
            )


    def crear(self, libro):

        libro_model = LibroModel(
            id=libro.id,
            isbn=libro.isbn,
            titulo=libro.titulo,
            autor=libro.autor,
            genero_id=libro.genero_id,
            editorial_id=libro.editorial_id
        )

        with self.db.get_session() as session:
            session.add(libro_model)
            return libro_model


    def actualizar(self,libro):
        with self.db.get_session() as session:
            session.merge(libro)

            return libro

    def eliminar(self,id_: int):
        with self.db.get_session() as session:
            libro = session.get(
                LibroModel,
                id_
            )
            if not libro:
                return False

            session.delete(libro)

            return True


class PrecioRepositorySQL:

    def __init__(self):
        self.db = ConexionDB()

    def leer_todos(self):
        with self.db.get_session() as session:
            return session.query(
                PrecioModel
            ).all()

    def leer_por_id(self,id_: int):
        with self.db.get_session() as session:
            return session.get(
                PrecioModel,
                id_
            )

    def crear(self,precio):
        precio_model = PrecioModel(
            id=precio.id,
            libro_id=precio.libro_id,
            moneda_id=precio.moneda_id,
            valor=precio.valor
        )
        with self.db.get_session() as session:
            session.add(precio_model)
            return precio_model

    def actualizar(self,precio):
        with self.db.get_session() as session:
            precio_model = session.get(
                PrecioModel,
                precio.id
            )
            if precio_model:

                precio_model.libro_id = precio.libro_id
                precio_model.moneda_id = precio.moneda_id
                precio_model.valor = precio.valor

            return precio_model

    def eliminar(self,id_: int):
        with self.db.get_session() as session:
            precio_model = session.get(
                PrecioModel,
                id_
            )
            if not precio_model:
                return False
            session.delete(precio_model)

            return True


class TipoCotizacionRepositorySQL:

    def __init__(self):
        self.db = ConexionDB()

    def leer_todos(self):
        with self.db.get_session() as session:
            return session.query(
                TipoCotizacionModel
            ).all()

    def leer_por_id(self,id_: int):
        with self.db.get_session() as session:
            return session.get(
                TipoCotizacionModel,
                id_
            )

    def crear(self,tipo):
        tipo_model = TipoCotizacionModel(
            id=tipo.id,
            nombre=tipo.nombre
        )
        with self.db.get_session() as session:
            session.add(tipo_model)
            return tipo_model

    def actualizar(self,tipo):
        with self.db.get_session() as session:
            tipo_model = session.get(
                TipoCotizacionModel,
                tipo.id
            )
            if tipo_model:
                tipo_model.nombre = tipo.nombre

            return tipo_model

    def eliminar(self,id_: int):
        with self.db.get_session() as session:
            tipo_model = session.get(
                TipoCotizacionModel,
                id_
            )
            if not tipo_model:
                return False

            session.delete(tipo_model)

            return True


class StockRepositorySQL:

    def __init__(self):
            self.db = ConexionDB()

    def leer_todos(self):
        with self.db.get_session() as session:
            return session.query(
                StockModel
            ).all()

    def leer_por_libro(self,libro_id):
        with self.db.get_session() as session:

            return session.get(
                StockModel,
                libro_id
            )

    def crear(self,stock):
        stock_model = StockModel(
            libro_id=stock.libro_id,
            cantidad=stock.cantidad
        )
        with self.db.get_session() as session:

            session.add(stock_model)

            return stock_model

    def actualizar(self,stock):
        with self.db.get_session() as session:

            stock_model = session.get(
                StockModel,
                stock.libro_id
            )
            if stock_model:
                stock_model.cantidad = stock.cantidad

            return stock_model

    def eliminar(self,libro_id):
        with self.db.get_session() as session:
            stock_model = session.get(
                StockModel,
                libro_id
            )
            if not stock_model:
                return False

            session.delete(stock_model)

            return True
    

class CotizacionDolarRepositorySQL:

    def __init__(self):
        self.db = ConexionDB()

    def leer_todos(self):
        with self.db.get_session() as session:
            return session.query(
                CotizacionDolarModel
            ).all()

    def crear(self,cotizacion):
        cotizacion_model = CotizacionDolarModel(
            tipo_id=cotizacion.tipo_id,
            fecha=cotizacion.fecha,
            valor=cotizacion.valor
        )
        with self.db.get_session() as session:
            session.add(cotizacion_model)

            return cotizacion_model

    def obtener(self,tipo_id,fecha):
        with self.db.get_session() as session:

            return session.get(
                CotizacionDolarModel,
                (tipo_id, fecha)
            )

    def actualizar(self,cotizacion):
        with self.db.get_session() as session:
            cotizacion_model = session.get(
                CotizacionDolarModel,
                (
                    cotizacion.tipo_id,
                    cotizacion.fecha
                )
            )
            if cotizacion_model:
                cotizacion_model.valor = cotizacion.valor

            return cotizacion_model
        
    
    def eliminar(self,tipo_id,fecha):
        with self.db.get_session() as session:
            cotizacion_model = session.get(
                CotizacionDolarModel,
                (tipo_id, fecha)
            )
            if not cotizacion_model:
                return False

            session.delete(cotizacion_model)

            return True


