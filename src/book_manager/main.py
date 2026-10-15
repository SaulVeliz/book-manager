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

from book_manager.repositories.repositories_sql import (
    LibroRepositorySQL,
    GeneroRepositorySQL,
    EditorialRepositorySQL,
    MonedaRepositorySQL,
    PrecioRepositorySQL,
    TipoCotizacionRepositorySQL,
    StockRepositorySQL,
    CotizacionDolarRepositorySQL
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


from book_manager.ui.console import (
    ConsoleUI
)

from book_manager.preload_data.csv_data import (
    cargar_generos,
    cargar_editoriales,
    cargar_monedas,
    cargar_libros,
    cargar_precios,
    cargar_stock,
    cargar_tipos_cotizacion,
    cargar_cotizaciones
)


def main():

    libro_repo = LibroRepositorySQL()
    genero_repo = GeneroRepositorySQL()
    editorial_repo = EditorialRepositorySQL()
    moneda_repo = MonedaRepositorySQL()
    precio_repo = PrecioRepositorySQL()
    tipo_repo = TipoCotizacionRepositorySQL()    
    stock_repo = StockRepositorySQL()
    cotizacion_repo = CotizacionDolarRepositorySQL()
    
#*****************************************************
#*****************************************************

    libro_service = LibroService(libro_repo)
    #for libro in cargar_libros():
    #        libro_service.crear(libro)
            
    genero_service = GeneroService(genero_repo)
    #for genero in cargar_generos():
    #        genero_service.crear(genero)

    editorial_service = EditorialService(editorial_repo)
    #for editorial in cargar_editoriales():
    #        editorial_service.crear(editorial)

    moneda_service = MonedaService(moneda_repo)
    #for moneda in cargar_monedas():
    #       moneda_service.crear(moneda)

    precio_service = PrecioService(precio_repo)
    #for precio in cargar_precios():
    #        precio_service.crear(precio)

    tipo_service = TipoCotizacionService(tipo_repo)
    #for tipo in cargar_tipos_cotizacion():
    #        tipo_service.crear(tipo)

    stock_service = StockService(stock_repo)
    #for stock in cargar_stock():
    #            stock_service.crear(stock)

    cotizacion_service = CotizacionDolarService(cotizacion_repo)
    #for cotizacion in cargar_cotizaciones():
    #    cotizacion_service.crear(cotizacion)

   

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