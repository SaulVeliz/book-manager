from abc import ABC, abstractmethod
from typing import Dict, Generic, List, Optional, TypeVar

from book_manager.entities.entities import (
EntidadBase,
Libro,
Genero,
Editorial,
Moneda,
TipoCotizacion,
Precio,
)

T = TypeVar("T", bound=EntidadBase)

class IRepositorio(ABC, Generic[T]):
    @abstractmethod
    def crear(self, entidad: T) -> T:
        pass

    @abstractmethod
    def leer_por_id(self, id_: int) -> Optional[T]:
        pass

    @abstractmethod
    def leer_todos(self) -> List[T]:
        pass

    @abstractmethod
    def actualizar(self, entidad: T) -> T:
        pass

    @abstractmethod
    def eliminar(self, id_: int) -> bool:
        pass


class RepositorioMemoria(IRepositorio[T]):

    def __init__(self):
        self._datos: Dict[int, T] = {}

    def crear(self, entidad: T) -> T:

        if entidad.id in self._datos:
            raise ValueError(
                f"Ya existe una entidad con id {entidad.id}"
            )

        self._datos[entidad.id] = entidad
        return entidad

    def leer_por_id(self, id_: int) -> Optional[T]:
        return self._datos.get(id_)
    
    def leer_todos(self) -> List:
        return list(self._datos.values())

    def actualizar(self, entidad: T) -> T:

        if entidad.id not in self._datos:
            raise ValueError(
                f"No existe una entidad con id {entidad.id}"
            )

        self._datos[entidad.id] = entidad
        return entidad

    def eliminar(self, id_: int) -> bool:

        if id_ not in self._datos:
            return False

        del self._datos[id_]
        return True


class LibroRepository(RepositorioMemoria[Libro]):
    pass


class GeneroRepository(RepositorioMemoria[Genero]):
    pass


class EditorialRepository(RepositorioMemoria[Editorial]):
    pass

class MonedaRepository(RepositorioMemoria[Moneda]):
    pass

class TipoCotizacionRepository(
    RepositorioMemoria[TipoCotizacion]
    ):
    pass

class PrecioRepository(
    RepositorioMemoria[Precio]
    ):
    pass


from book_manager.entities.entities import (
    EntidadBase,
    Libro,
    Genero,
    Editorial,
    Moneda,
    TipoCotizacion,
    Precio,
    Stock,
    CotizacionDolar,
)


class StockRepository:

    def __init__(self):
        self._datos = {}

    def crear(self, stock: Stock):

        if stock.libro_id in self._datos:
            raise ValueError(
                f"Ya existe stock para libro {stock.libro_id}"
            )

        self._datos[stock.libro_id] = stock
        return stock

    def leer_por_libro(self, libro_id: int):

        return self._datos.get(libro_id)

    def actualizar(self, stock: Stock):

        if stock.libro_id not in self._datos:
            raise ValueError(
                f"No existe stock para libro {stock.libro_id}"
            )

        self._datos[stock.libro_id] = stock

        return stock

    def eliminar(self, libro_id: int):

        if libro_id not in self._datos:
            return False

        del self._datos[libro_id]
        return True


class CotizacionDolarRepository:

    def __init__(self):
        self._datos = {}

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

    def leer_por_tipo_y_fecha(self,tipo_id,fecha):

        return self._datos.get((tipo_id, fecha)
        )

    def leer_historico_por_tipo(self,tipo_id):

        return [
            c
            for c in self._datos.values()
            if c.tipo_id == tipo_id
        ]

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

        clave = (tipo_id, fecha)

        if clave not in self._datos:
            return False

        del self._datos[clave]

        return True


    