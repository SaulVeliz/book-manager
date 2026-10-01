from dataclasses import dataclass
from datetime import date


@dataclass
class EntidadBase:
    id: int

@dataclass
class Libro(EntidadBase):
    isbn: str
    titulo: str
    autor: str
    genero_id: int
    editorial_id: int

@dataclass
class Genero(EntidadBase):
    nombre: str
    descripcion: str


@dataclass
class Editorial(EntidadBase):
    nombre: str
    pais: str


@dataclass
class Moneda(EntidadBase):
    codigo: str
    nombre: str
    simbolo: str


@dataclass
class TipoCotizacion(EntidadBase):
    nombre: str


@dataclass
class Precio(EntidadBase):
    libro_id: int
    moneda_id: int
    valor: float


@dataclass
class Stock:
    libro_id: int
    cantidad: int


@dataclass
class CotizacionDolar:
    tipo_id: int
    fecha: date
    valor: float


