SELECT c.Codigo_casamiento, COUNT(o.Codigo_envio) AS Cantidad_envios
FROM Casamiento c
LEFT JOIN Ordenes_envio o ON c.Codigo_casamiento = o.Codigo_casamiento
WHERE c.Fecha >= '2021-06-01'
GROUP BY c.Codigo_casamiento;