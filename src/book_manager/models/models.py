from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import (
    Integer,
    String,
    Float,
    Date,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)


class Base(DeclarativeBase):
    pass


class GeneroModel(Base):

    __tablename__ = "generos"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    nombre: Mapped[str] = mapped_column(
        String(100)
    )

    descripcion: Mapped[str] = mapped_column(
        String(255)
    )

    def __str__(self):
        return (
            f"[{self.id}] "
            f"{self.nombre} - "
            f"{self.descripcion}"
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


class EditorialModel(Base):

    __tablename__ = "editoriales"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    nombre: Mapped[str] = mapped_column(
        String(100)
    )

    pais: Mapped[str] = mapped_column(
        String(100)
    )

    def __str__(self):
        return (
            f"[{self.id}] "
            f"{self.nombre} - "
            f"{self.pais}"
        )


class MonedaModel(Base):

    __tablename__ = "monedas"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    codigo: Mapped[str] = mapped_column(
        String(10)
    )

    nombre: Mapped[str] = mapped_column(
        String(100)
    )

    simbolo: Mapped[str] = mapped_column(
        String(20)
    )

    def __str__(self):
        return (
            f"[{self.id}] "
            f"{self.codigo} - "
            f"{self.nombre}"
        )


class TipoCotizacionModel(Base):

    def __str__(self):
        return (
            f"[{self.id}] "
            f"{self.nombre}"
        )

    __tablename__ = "tipos_cotizacion"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    nombre: Mapped[str] = mapped_column(
        String(100)
    )


class LibroModel(Base):

    __tablename__ = "libros"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    isbn: Mapped[str] = mapped_column(
        String(50)
    )

    titulo: Mapped[str] = mapped_column(
        String(255)
    )

    autor: Mapped[str] = mapped_column(
        String(255)
    )

    genero_id: Mapped[int] = mapped_column(
        ForeignKey("generos.id")
    )

    editorial_id: Mapped[int] = mapped_column(
        ForeignKey("editoriales.id")
    )

    def __str__(self):
        return (
            f"[{self.id}] "
            f"{self.titulo} - "
            f"{self.autor}"
        )


class PrecioModel(Base):

    def __str__(self):

        return (
            f"[{self.id}] "
            f"Libro:{self.libro_id} "
            f"Moneda:{self.moneda_id} "
            f"Precio:${self.valor}"
        )

    __tablename__ = "precios"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    libro_id: Mapped[int] = mapped_column(
        ForeignKey("libros.id")
    )

    moneda_id: Mapped[int] = mapped_column(
        ForeignKey("monedas.id")
    )

    valor: Mapped[float] = mapped_column(
        Float
    )


class StockModel(Base):

    def __str__(self):
        return (
            f"Libro:{self.libro_id} "
            f"Cantidad:{self.cantidad}"
        )

    __tablename__ = "stock"

    libro_id: Mapped[int] = mapped_column(
        ForeignKey("libros.id"),
        primary_key=True
    )

    cantidad: Mapped[int] = mapped_column(
        Integer
    )


class CotizacionDolarModel(Base):

    def __str__(self):

        nombres = {
            1: "Oficial",
            2: "Blue",
            3: "MEP",
            4: "CCL",
            5: "Tarjeta"
        }

        nombre_tipo = nombres.get(
            self.tipo_id,
            f"Tipo {self.tipo_id}"
        )

        return (
            f"{nombre_tipo}: "
            f"{self.fecha} --> "
            f"${self.valor}"
        )

    __tablename__ = "cotizaciones_dolar"

    tipo_id: Mapped[int] = mapped_column(
        ForeignKey("tipos_cotizacion.id"),
        primary_key=True
    )

    fecha: Mapped[Date] = mapped_column(
        Date,
        primary_key=True
    )

    valor: Mapped[float] = mapped_column(
        Float
    )
