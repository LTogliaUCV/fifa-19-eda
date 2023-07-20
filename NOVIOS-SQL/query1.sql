SELECT c.Codigo_casamiento, c.Fecha, r.Codigo_articulo, a.Nombre_articulo, r.Cantidad_requerida, r.Regalado
FROM Casamiento c
JOIN Regalos r ON c.Codigo_casamiento = r.Codigo_casamiento
JOIN Articulos a ON r.Codigo_articulo = a.Codigo_articulo
WHERE c.Fecha > '2022-01-01' AND a.Cantidad_stock < 10;

