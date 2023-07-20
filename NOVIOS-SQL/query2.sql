SELECT a.Nombre_articulo, SUM(r.Cantidad_requerida) AS Total_requerido
FROM Articulos a
JOIN Regalos r ON a.Codigo_articulo = r.Codigo_articulo
WHERE r.Regalado = 'N' AND a.Precio > 500
GROUP BY a.Nombre_articulo
HAVING SUM(r.Cantidad_requerida) > 100;