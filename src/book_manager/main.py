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

from book_manager.services.services import (
    LibroService,
    GeneroService,
    EditorialService,
    MonedaService,
    TipoCotizacionService,
    PrecioService,
    StockService,
    CotizacionDolarService,
)

from book_manager.preload_data.preload_data import (
    cargar_generos,
    cargar_editoriales,
    cargar_monedas,
    cargar_tipos_cotizacion,
    cargar_libros,
    cargar_precios,
)


from book_manager.ui.console import (
    ConsoleUI
)

from book_manager.preload_data.csv_data import (
    cargar_generos,
    cargar_editoriales,
    cargar_monedas,
    cargar_libros,
    cargar_precios
)


def main():

    genero_repo = GeneroRepository()
    editorial_repo = EditorialRepository()
    moneda_repo = MonedaRepository()
    tipo_repo = TipoCotizacionRepository()
    libro_repo = LibroRepository()
    precio_repo = PrecioRepository()
    stock_repo = StockRepository()
    cotizacion_repo = CotizacionDolarRepository()


    genero_service = GeneroService(genero_repo)
    editorial_service = EditorialService(editorial_repo)
    moneda_service = MonedaService(moneda_repo)
    tipo_service = TipoCotizacionService(tipo_repo)
    libro_service = LibroService(libro_repo)
    precio_service = PrecioService(precio_repo)
    stock_service = StockService(stock_repo)
    cotizacion_service = CotizacionDolarService(cotizacion_repo)


    for libro in cargar_libros():
        libro_service.crear(libro)
    
    for genero in cargar_generos():
        genero_service.crear(genero)


    for editorial in cargar_editoriales():
        editorial_service.crear(editorial)

    for moneda in cargar_monedas():
        moneda_service.crear(moneda)

    for tipo in cargar_tipos_cotizacion():
        tipo_service.crear(tipo)

    for precio in cargar_precios():
        precio_service.crear(precio)


    ui = ConsoleUI(
    libro_service,
    genero_service,
    editorial_service,
    moneda_service,
    precio_service,
    tipo_service,
    stock_service,
    cotizacion_service
    )

    ui.mostrar_menu()


if __name__ == "__main__":
    main()