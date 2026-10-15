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
            
    genero_service = GeneroService(genero_repo)

    editorial_service = EditorialService(editorial_repo)

    moneda_service = MonedaService(moneda_repo)

    precio_service = PrecioService(precio_repo)

    tipo_service = TipoCotizacionService(tipo_repo)

    stock_service = StockService(stock_repo)

    cotizacion_service = CotizacionDolarService(cotizacion_repo)

   

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