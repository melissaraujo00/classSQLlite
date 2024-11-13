from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Autor(Base):
    __tablename__ = 'tbl_autor'

    id_autor = Column(Integer, primary_key = True, autoincrement=True)
    nombre = Column(String, nullable = False)
    pais = Column(String, nullable = False)

    libros = relationship("Libro", back_populates="autor")

class Libro(Base):
    __tablename__ = 'tbl_libro'

    id_libro = Column(Integer, primary_key = True, autoincrement=True)
    titulo = Column(String, nullable = False)
    genero = Column(String,nullable = False)
    fecha_publicacion = Column(Date)
    id_autor = Column(Integer, ForeignKey('tbl_autor.id_autor'))

    autor = relationship("Autor", back_populates="libro")
    prestamo = relationship("Prestamo", back_populates = "libro")

class Prestamo(Base):
    __tablename__ = 'prestamos'
    id_prestamo = Column(Integer, primary_key=True, autoincrement=True)
    fecha_prestamo = Column(Date, nullable=False)
    fecha_devolucion = Column(Date)
    usuario = Column(String, nullable=False)  
    id_libro = Column(Integer, ForeignKey('tbl_libro.id_libro'))

    libro = relationship("Libro", back_populates="prestamos")


engine = create_engine('sqlite:///biblioteca.db', echo=True)

Base.metadata.create_all(engine)

