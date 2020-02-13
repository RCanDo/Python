SELECT b.name, count(*) nr_of 
FROM albums a INNER JOIN artists b USING(ArtistId)
GROUP BY b.name
ORDER BY 2 DESC, 1