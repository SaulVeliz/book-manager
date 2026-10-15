import csv
from datetime import date
from pathlib import Path

from book_manager.database.connection import ConexionDB

from book_manager.models.models import (
    GeneroModel,
    EditorialModel,
    MonedaModel,
    TipoCotizacionModel,
    LibroModel,
    PrecioModel,
    StockModel,
    CotizacionDolarModel

)


def migrar_datos(
    carpeta_csvs: str,
    carpeta_sqls: str
):
    """
    Lee los CSV del TP1
    y genera archivos SQL
    con sentencias INSERT.
    """

    carpeta_csvs = Path(carpeta_csvs)
    carpeta_sqls = Path(carpeta_sqls)

    carpeta_sqls.mkdir(
        parents=True,
        exist_ok=True
    )

    for archivo_csv in carpeta_csvs.glob("*.csv"):

        nombre_tabla = archivo_csv.stem

        archivo_sql = (
            carpeta_sqls /
            f"{nombre_tabla}.sql"
        )

        with open(
            archivo_csv,
            mode="r",
            encoding="utf-8-sig"
        ) as csv_file:

            lector = csv.DictReader(csv_file)

            with open(
                archivo_sql,
                mode="w",
                encoding="utf-8"
            ) as sql_file:

                for fila in lector:

                    columnas = ", ".join(
                        fila.keys()
                    )

                    valores = ", ".join(
                        [
                            f"'{valor}'"
                            for valor in fila.values()
                        ]
                    )

                    sentencia = (
                        f"INSERT INTO {nombre_tabla} "
                        f"({columnas}) "
                        f"VALUES ({valores});\n"
                    )

                    sql_file.write(
                        sentencia
                    )


def migrar_generos_csv():

    db = ConexionDB()

    with open(
        "book_manager/migrations/csv/generos.csv",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        with db.get_session() as session:

            for fila in lector:

                session.add(
                    GeneroModel(
                        id=int(fila["id"]),
                        nombre=fila["nombre"],
                        descripcion=fila["descripcion"]
                    )
                )


def migrar_editoriales_csv():

    db = ConexionDB()

    with open(
        "book_manager/migrations/csv/editoriales.csv",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        with db.get_session() as session:

            for fila in lector:

                session.add(
                    EditorialModel(
                        id=int(fila["id"]),
                        nombre=fila["nombre"],
                        pais=fila["pais"]
                    )
                )


def migrar_monedas_csv():

    db = ConexionDB()

    with open(
        "book_manager/migrations/csv/monedas.csv",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        with db.get_session() as session:

            for fila in lector:

                session.add(
                    MonedaModel(
                        id=int(fila["id"]),
                        codigo=fila["codigo"],
                        nombre=fila["nombre"],
                        simbolo=fila["simbolo"]
                    )
                )


def migrar_tipos_cotizacion_csv():

    db = ConexionDB()

    with open(
        "book_manager/migrations/csv/tipos_cotizacion.csv",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        with db.get_session() as session:

            for fila in lector:

                session.add(
                    TipoCotizacionModel(
                        id=int(fila["id"]),
                        nombre=fila["nombre"]
                    )
                )


def migrar_libros_csv():

    db = ConexionDB()

    with open(
        "book_manager/migrations/csv/libros.csv",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        with db.get_session() as session:

            for fila in lector:

                session.add(
                    LibroModel(
                        id=int(fila["id"]),
                        isbn=fila["isbn"],
                        titulo=fila["titulo"],
                        autor=fila["autor"],
                        genero_id=int(fila["genero_id"]),
                        editorial_id=int(fila["editorial_id"])
                    )
                )


def migrar_precios_csv():

    db = ConexionDB()

    with open(
        "book_manager/migrations/csv/precios.csv",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        with db.get_session() as session:

            for fila in lector:

                session.add(
                    PrecioModel(
                        id=int(fila["id"]),
                        libro_id=int(fila["libro_id"]),
                        moneda_id=int(fila["moneda_id"]),
                        valor=float(fila["valor"])
                    )
                )


def migrar_stock_csv():

    db = ConexionDB()

    with open(
        "book_manager/migrations/csv/stock.csv",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        with db.get_session() as session:

            for fila in lector:

                session.add(
                    StockModel(
                        libro_id=int(fila["libro_id"]),
                        cantidad=int(fila["cantidad"])
                    )
                )


def migrar_cotizaciones_csv():

    db = ConexionDB()

    with open(
        "book_manager/migrations/csv/cotizaciones.csv",
        encoding="utf-8-sig"
    ) as archivo:

        lector = csv.DictReader(archivo)

        with db.get_session() as session:

            for fila in lector:

                session.add(
                    CotizacionDolarModel(
                        tipo_id=int(fila["tipo_id"]),
                        fecha=date.fromisoformat(
                            fila["fecha"]
                        ),
                        valor=float(
                            fila["valor"]
                        )
                    )
                )


def migrar_datos():

    migrar_generos_csv()
    migrar_editoriales_csv()
    migrar_monedas_csv()
    migrar_tipos_cotizacion_csv()
    migrar_libros_csv()
    migrar_precios_csv()
    migrar_stock_csv()
    migrar_cotizaciones_csv()