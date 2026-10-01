from book_manager.entities.entities import (
Genero,
Editorial,
Moneda,
TipoCotizacion,
Libro,
Precio,
)


def cargar_generos():

    return [
        Genero(1, "Novela", "Literatura narrativa"),
        Genero(2, "Ciencia Ficcion", "Futuro y tecnologia"),
        Genero(3, "Terror", "Historias de miedo"),
        Genero(4, "Fantasia", "Mundos imaginarios"),
        Genero(5, "Historia", "Eventos historicos"),
        Genero(6, "Tecnologia", "Libros tecnicos"),
        Genero(7, "Programacion", "Desarrollo de software"),
        Genero(8, "Matematica", "Numeros y calculo"),
        Genero(9, "Ciencia", "Investigacion cientifica"),
        Genero(10, "Educacion", "Material educativo"),
    ]


def cargar_editoriales():

    return [
        Editorial(1, "Planeta", "Argentina"),
        Editorial(2, "Sudamericana", "Argentina"),
        Editorial(3, "Penguin", "Estados Unidos"),
        Editorial(4, "Anaya", "España"),
        Editorial(5, "Alfaomega", "Mexico"),
        Editorial(6, "OReilly", "Estados Unidos"),
        Editorial(7, "McGraw Hill", "Estados Unidos"),
        Editorial(8, "Pearson", "Reino Unido"),
        Editorial(9, "Kapelusz", "Argentina"),
        Editorial(10, "Aique", "Argentina"),
    ]


def cargar_monedas():

    return [
        Moneda(1, "ARS", "Peso Argentino", "$"),
        Moneda(2, "USD", "Dolar Estadounidense", "US$"),
        Moneda(3, "EUR", "Euro", "€"),
        Moneda(4, "GBP", "Libra Esterlina", "£"),
        Moneda(5, "BRL", "Real", "R$"),
        Moneda(6, "UYU", "Peso Uruguayo", "$U"),
        Moneda(7, "CLP", "Peso Chileno", "$CL"),
        Moneda(8, "PYG", "Guarani", "Gs"),
        Moneda(9, "JPY", "Yen", "¥"),
        Moneda(10, "CHF", "Franco Suizo", "CHF"),
    ]


def cargar_tipos_cotizacion():

    return [
        TipoCotizacion(1, "Oficial"),
        TipoCotizacion(2, "Blue"),
        TipoCotizacion(3, "MEP"),
        TipoCotizacion(4, "CCL"),
        TipoCotizacion(5, "Tarjeta"),
        TipoCotizacion(6, "Mayorista"),
        TipoCotizacion(7, "Minorista"),
        TipoCotizacion(8, "Turista"),
        TipoCotizacion(9, "Cripto"),
        TipoCotizacion(10, "Banco Nacion"),
    ]


def cargar_libros():

    return [
        Libro(1, "978950001", "Fundacion", "Isaac Asimov", 2, 1),
        Libro(2, "978950002", "Yo Robot", "Isaac Asimov", 2, 1),
        Libro(3, "978950003", "Dracula", "Bram Stoker", 3, 2),
        Libro(4, "978950004", "El Hobbit", "J. R. R. Tolkien", 4, 3),
        Libro(5, "978950005", "Breve Historia del Tiempo", "Stephen Hawking", 9, 4),
        Libro(6, "978950006", "Python para Todos", "Charles Severance", 7, 5),
        Libro(7, "978950007", "Calculo I", "James Stewart", 8, 6),
        Libro(8, "978950008", "Redes de Computadoras", "Andrew Tanenbaum", 6, 7),
        Libro(9, "978950009", "Didactica General", "Alicia Camilloni", 10, 8),
        Libro(10, "978950010", "Sapiens", "Yuval Noah Harari", 5, 9),
    ]


def cargar_precios():

    return [
        Precio(1, 1, 1, 25000.0),
        Precio(2, 2, 1, 22000.0),
        Precio(3, 3, 1, 18000.0),
        Precio(4, 4, 1, 30000.0),
        Precio(5, 5, 1, 35000.0),
        Precio(6, 6, 1, 28000.0),
        Precio(7, 7, 1, 32000.0),
        Precio(8, 8, 1, 27000.0),
        Precio(9, 9, 1, 21000.0),
        Precio(10, 10, 1, 40000.0),
    ]