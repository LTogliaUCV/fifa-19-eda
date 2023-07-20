CREATE TABLE Novios (
  Codigo_casamiento TEXT,
  Nombre_novio VARCHAR(255),
  Apellido_novio VARCHAR(255),
  PRIMARY KEY (Codigo_casamiento)
);

CREATE TABLE Casamiento (
  Codigo_casamiento TEXT,
  Fecha TIMESTAMP,
  Comentario VARCHAR(255),
  PRIMARY KEY (Codigo_casamiento)
);

CREATE TABLE Articulos (
  Codigo_articulo TEXT,
  Precio FLOAT,
  Cantidad_stock INTEGER,
  Nombre_articulo VARCHAR(255),
  PRIMARY KEY (Codigo_articulo)
);

CREATE TABLE Regalos (
  Codigo_articulo TEXT,
  Codigo_casamiento TEXT,
  Cantidad_requerida INTEGER,
  Regalado BOOLEAN,
  PRIMARY KEY (Codigo_articulo, Codigo_casamiento),
  FOREIGN KEY (Codigo_articulo) REFERENCES Articulos(Codigo_articulo),
  FOREIGN KEY (Codigo_casamiento) REFERENCES Casamiento(Codigo_casamiento)
);

CREATE TABLE Ordenes_envio (
  Codigo_envio TEXT,
  Codigo_casamiento TEXT,
  Fecha_envio TIMESTAMP,
  PRIMARY KEY (Codigo_envio),
  FOREIGN KEY (Codigo_casamiento) REFERENCES Casamiento(Codigo_casamiento)
);

CREATE TABLE Detalle_envio (
  Codigo_envio TEXT,
  Codigo_articulo TEXT,
  Cantidad_enviada INTEGER,
  PRIMARY KEY (Codigo_envio, Codigo_articulo),
  FOREIGN KEY (Codigo_envio) REFERENCES Ordenes_envio(Codigo_envio),
  FOREIGN KEY (Codigo_articulo) REFERENCES Articulos(Codigo_articulo)
);