from datetime import date
import csv
from book_manager.entities.entities import (
    Genero,
    Editorial,
    Moneda,
    Libro,
    Precio,
    Stock,
    TipoCotizacion,
    CotizacionDolar
)

ARCHIVO = "book_manager/migrations/csv/generos.csv"
ARCHIVO_EDITORIALES = ("book_manager/migrations/csv/editoriales.csv")
ARCHIVO_MONEDAS = ("book_manager/migrations/csv/monedas.csv")
ARCHIVO_LIBROS = ("book_manager/migrations/csv/libros.csv")
ARCHIVO_PRECIOS = ("book_manager/migrations/csv/precios.csv")
ARCHIVO_STOCK = ("book_manager/migrations/csv/stock.csv")
ARCHIVO_TIPOS_COTIZACION = ("book_manager/migrations/csv/tipos_cotizacion.csv")
ARCHIVO_COTIZACIONES = ("book_manager/migrations/csv/cotizaciones.csv")


#***********************************************************************************
#***********************************************************************************
# #funciones CRUD Libro

def cargar_libros():

    libros = []

    with open(
        ARCHIVO_LIBROS,
        mode="r",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            libros.append(
                Libro(
                    id=int(fila["id"]),
                    isbn=fila["isbn"],
                    titulo=fila["titulo"],
                    autor=fila["autor"],
                    genero_id=int(
                        fila["genero_id"]
                    ),
                    editorial_id=int(
                        fila["editorial_id"]
                    )
                )
            )

    return libros


def guardar_todos_los_libros(
    libros
):

    with open(
        ARCHIVO_LIBROS,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as archivo:

        writer = csv.writer(archivo)

        writer.writerow(
            [
                "id",
                "isbn",
                "titulo",
                "autor",
                "genero_id",
                "editorial_id"
            ]
        )

        for libro in libros:

            writer.writerow(
                [
                    libro.id,
                    libro.isbn,
                    libro.titulo,
                    libro.autor,
                    libro.genero_id,
                    libro.editorial_id
                ]
            )


#***********************************************************************************
#***********************************************************************************
#funciones CRUD Genero

def guardar_genero(id_, nombre, descripcion):

    with open(
        ARCHIVO,
        mode="a",
        newline="",
        encoding="utf-8-sig"
    ) as archivo:

        writer = csv.writer(archivo)

        writer.writerow(
            [
                id_,
                nombre,
                descripcion
            ]
        )


def cargar_generos():

    generos = []

    with open(
        ARCHIVO,
        mode="r",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            generos.append(
                Genero(
                    id=int(fila["id"]),
                    nombre=fila["nombre"],
                    descripcion=fila["descripcion"]
                )
            )

    return generos


def guardar_todos_los_generos(generos):

    with open(
        ARCHIVO,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as archivo:

        writer = csv.writer(archivo)

        writer.writerow(
            [
                "id",
                "nombre",
                "descripcion"
            ]
        )

        for genero in generos:

            writer.writerow(
                [
                    genero.id,
                    genero.nombre,
                    genero.descripcion
                ]
            )


#***********************************************************************************
#***********************************************************************************
#funciones CRUD Editoriales

def cargar_editoriales():

    editoriales = []

    with open(
        ARCHIVO_EDITORIALES,
        mode="r",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            editoriales.append(
                Editorial(
                    id=int(fila["id"]),
                    nombre=fila["nombre"],
                    pais=fila["pais"]
                )
            )

    return editoriales


def guardar_todas_las_editoriales(
    editoriales
):

    with open(
        ARCHIVO_EDITORIALES,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as archivo:

        writer = csv.writer(
            archivo
        )

        writer.writerow(
            [
                "id",
                "nombre",
                "pais"
            ]
        )

        for editorial in editoriales:

            writer.writerow(
                [
                    editorial.id,
                    editorial.nombre,
                    editorial.pais
                ]
            )


#***********************************************************************************
#***********************************************************************************
#funciones CRUD Monedas

def cargar_monedas():

    monedas = []

    with open(
        ARCHIVO_MONEDAS,
        mode="r",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            monedas.append(
                Moneda(
                    id=int(fila["id"]),
                    codigo=fila["codigo"],
                    nombre=fila["nombre"],
                    simbolo=fila["simbolo"]
                )
            )

    return monedas


def guardar_todas_las_monedas(
    monedas
):

    with open(
        ARCHIVO_MONEDAS,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as archivo:

        writer = csv.writer(archivo)

        writer.writerow(
            [
                "id",
                "codigo",
                "nombre",
                "simbolo"
            ]
        )

        for moneda in monedas:

            writer.writerow(
                [
                    moneda.id,
                    moneda.codigo,
                    moneda.nombre,
                    moneda.simbolo
                ]
            )


#***********************************************************************************
#***********************************************************************************
#funciones CRUD Precios

def cargar_precios():

    precios = []

    with open(
        ARCHIVO_PRECIOS,
        mode="r",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            precios.append(
                Precio(
                    id=int(fila["id"]),
                    libro_id=int(
                        fila["libro_id"]
                    ),
                    moneda_id=int(
                        fila["moneda_id"]
                    ),
                    valor=float(
                        fila["valor"]
                    )
                )
            )

    return precios


def guardar_todos_los_precios(
    precios
):

    with open(
        ARCHIVO_PRECIOS,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as archivo:

        writer = csv.writer(archivo)

        writer.writerow(
            [
                "id",
                "libro_id",
                "moneda_id",
                "valor"
            ]
        )

        for precio in precios:

            writer.writerow(
                [
                    precio.id,
                    precio.libro_id,
                    precio.moneda_id,
                    precio.valor
                ]
            )


#***********************************************************************************
#***********************************************************************************
#funciones CRUD Tipo de Cotizaciones

def cargar_tipos_cotizacion():

    tipos = []

    with open(
        ARCHIVO_TIPOS_COTIZACION,
        mode="r",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            tipos.append(
                TipoCotizacion(
                    id=int(fila["id"]),
                    nombre=fila["nombre"]
                )
            )

    return tipos


def guardar_todos_los_tipos_cotizacion(
    tipos
):

    with open(
        ARCHIVO_TIPOS_COTIZACION,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as archivo:

        writer = csv.writer(archivo)

        writer.writerow(
            ["id", "nombre"]
        )

        for tipo in tipos:

            writer.writerow(
                [
                    tipo.id,
                    tipo.nombre
                ]
            )


#***********************************************************************************
#***********************************************************************************
#funciones CRUD Stock

def cargar_stock():

    stocks = []

    with open(
        ARCHIVO_STOCK,
        mode="r",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            stocks.append(
                Stock(
                    libro_id=int(
                        fila["libro_id"]
                    ),
                    cantidad=int(
                        fila["cantidad"]
                    )
                )
            )

    return stocks


def guardar_todos_los_stock(stocks):

    with open(
        ARCHIVO_STOCK,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as archivo:

        writer = csv.writer(archivo)

        writer.writerow(
            [
                "libro_id",
                "cantidad"
            ]
        )

        for stock in stocks:

            writer.writerow(
                [
                    stock.libro_id,
                    stock.cantidad
                ]
            )


#***********************************************************************************
#***********************************************************************************
#funciones CRUD Cotizaciones Dolar

def cargar_cotizaciones():

    cotizaciones = []

    with open(
        ARCHIVO_COTIZACIONES,
        mode="r",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            cotizaciones.append(
                CotizacionDolar(
                    tipo_id=int(
                        fila["tipo_id"]
                    ),
                    fecha=date.fromisoformat(
                        fila["fecha"]
                    ),
                    valor=float(
                        fila["valor"]
                    )
                )
            )

    return cotizaciones


def guardar_todas_las_cotizaciones(
    cotizaciones
):

    with open(
        ARCHIVO_COTIZACIONES,
        mode="w",
        newline="",
        encoding="utf-8-sig"
    ) as archivo:

        writer = csv.writer(archivo)

        writer.writerow(
            [
                "tipo_id",
                "fecha",
                "valor"
            ]
        )

        for cotizacion in cotizaciones:

            writer.writerow(
                [
                    cotizacion.tipo_id,
                    cotizacion.fecha,
                    cotizacion.valor
                ]
            )