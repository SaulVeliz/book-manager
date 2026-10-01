from book_manager.entities.entities import (
    Libro,
    Genero,
    Editorial,
    Moneda,
    TipoCotizacion,
    Precio,
)

from book_manager.repositories.repositories import (
    LibroRepository,
    GeneroRepository,
    EditorialRepository,
    MonedaRepository,
    TipoCotizacionRepository,
    PrecioRepository,
)

from book_manager.entities.entities import (
    Libro,
    Genero,
    Editorial,
    Moneda,
    TipoCotizacion,
    Precio,
    Stock,
    CotizacionDolar,
)

from book_manager.repositories.repositories import (
    LibroRepository,
    GeneroRepository,
    EditorialRepository,
    MonedaRepository,
    TipoCotizacionRepository,
    PrecioRepository,
    StockRepository,
    CotizacionDolarRepository,
)



class LibroService:

    def __init__(
        self,
        libro_repo: LibroRepository
    ):
        self._libro_repo = libro_repo
    
    def crear(self, libro: Libro):    
        return self._libro_repo.crear(libro)
    
    def obtener_por_id(self, id_: int):
        return self._libro_repo.leer_por_id(id_)
    
    def listar(self):
        return self._libro_repo.leer_todos()
    
    def actualizar(self, libro: Libro):
        return self._libro_repo.actualizar(libro)
    
    def eliminar(self, id_: int):
        return self._libro_repo.eliminar(id_)


class GeneroService:

    def __init__(
        self,
        genero_repo: GeneroRepository
    ):
        self._genero_repo = genero_repo

    def crear(self, genero: Genero):
        return self._genero_repo.crear(genero)

    def obtener_por_id(self, id_: int):
        return self._genero_repo.leer_por_id(id_)

    def listar(self):
        return self._genero_repo.leer_todos()

    def actualizar(self, genero: Genero):
        return self._genero_repo.actualizar(genero)

    def eliminar(self, id_: int):
        return self._genero_repo.eliminar(id_)


class EditorialService:

    def __init__(
        self,
        editorial_repo: EditorialRepository
    ):
        self._editorial_repo = editorial_repo
    
    def crear(self, editorial: Editorial):
        return self._editorial_repo.crear(editorial)
    
    def obtener_por_id(self, id_: int):
        return self._editorial_repo.leer_por_id(id_)
    
    def listar(self):
        return self._editorial_repo.leer_todos()
    
    def actualizar(self, editorial: Editorial):
        return self._editorial_repo.actualizar(editorial)
    
    def eliminar(self, id_: int):
        return self._editorial_repo.eliminar(id_)
    

class MonedaService:
    
    def __init__(
        self,
        moneda_repo: MonedaRepository
    ):
        self._moneda_repo = moneda_repo
    
    def crear(self, moneda: Moneda):
        return self._moneda_repo.crear(moneda)
    
    def obtener_por_id(self, id_: int):
        return self._moneda_repo.leer_por_id(id_)
    
    def listar(self):
        return self._moneda_repo.leer_todos()
    
    def actualizar(self, moneda: Moneda):
        return self._moneda_repo.actualizar(moneda)
    
    def eliminar(self, id_: int):
        return self._moneda_repo.eliminar(id_)


class TipoCotizacionService:
    
    def __init__(
        self,
        tipo_repo: TipoCotizacionRepository
    ):
        self._tipo_repo = tipo_repo
    
    def crear(self, tipo: TipoCotizacion):
        return self._tipo_repo.crear(tipo)
    
    def obtener_por_id(self, id_: int):
        return self._tipo_repo.leer_por_id(id_)
    
    def listar(self):
        return self._tipo_repo.leer_todos()
    
    def actualizar(self, tipo: TipoCotizacion):
        return self._tipo_repo.actualizar(tipo)
    
    def eliminar(self, id_: int):
        return self._tipo_repo.eliminar(id_)


class PrecioService:

    def __init__(
        self,
        precio_repo: PrecioRepository
    ):
        self._precio_repo = precio_repo
    
    def crear(self, precio: Precio):
        return self._precio_repo.crear(precio)
    
    def obtener_por_id(self, id_: int):
        return self._precio_repo.leer_por_id(id_)
    
    def listar(self):
        return self._precio_repo.leer_todos()
    
    def actualizar(self, precio: Precio):
        return self._precio_repo.actualizar(precio)
    
    def eliminar(self, id_: int):
        return self._precio_repo.eliminar(id_)


class StockService:

    def __init__(
        self,
        stock_repo: StockRepository
    ):
        self._stock_repo = stock_repo

    def crear(self, stock: Stock):

        return self._stock_repo.crear(stock)

    def obtener_por_libro(
        self,
        libro_id: int
    ):

        return self._stock_repo.leer_por_libro(
            libro_id
        )

    def actualizar(
        self,
        stock: Stock
    ):

        return self._stock_repo.actualizar(stock)

    def eliminar(
        self,
        libro_id: int
    ):

        return self._stock_repo.eliminar(
            libro_id
        )


class CotizacionDolarService:

    def __init__(
        self,
        cotizacion_repo: CotizacionDolarRepository
    ):
        self._cotizacion_repo = cotizacion_repo

    def crear(
        self,
        cotizacion: CotizacionDolar
    ):

        return self._cotizacion_repo.crear(
            cotizacion
        )

    def obtener(
        self,
        tipo_id,
        fecha
    ):

        return self._cotizacion_repo.leer_por_tipo_y_fecha(
            tipo_id,
            fecha
        )

    def historico(
        self,
        tipo_id
    ):

        return self._cotizacion_repo.leer_historico_por_tipo(
            tipo_id
        )

    def actualizar(
        self,
        cotizacion
    ):

        return self._cotizacion_repo.actualizar(
            cotizacion
        )

    def eliminar(
        self,
        tipo_id,
        fecha
    ):

        return self._cotizacion_repo.eliminar(
            tipo_id,
            fecha
        )


