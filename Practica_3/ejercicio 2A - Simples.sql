-- EJERCIO 2: Simples sobre una sola tabla
-- 1. La poblacion de Argentina
SELECT country.population as Poblacion_Argentina FROM country WHERE country.name = 'Argentina';

-- 2. Todos los continentes (sin repeticiones)
SELECT DISTINCT country.continent as Continentes FROM country;

-- 3. Nombres de los paıses de America del Sur con mas de 15 millones de habitantes
SELECT DISTINCT country.name as Paises_Mas_Poblacion FROM country WHERE country.population > 15000000 and country.continent = 'South America';

-- 4. Nombre y producto bruto de los diez pa´ıses con mayor producto bruto (gnp)
SELECT DISTINCT country.name AS Pais, country.gnp AS Producto FROM country ORDER BY country.gnp DESC; -- limit 10


-- 5. Forma de gobierno y cantidad de paises con dicha forma de gobierno ordenados por cantidad de modo descendente
-- (sugerencia: agrupar por forma de gobierno y contar)
SELECT DISTINCT country.governmentform AS Forma_de_gobierno, COUNT(country.governmentform) AS Cantidad_Paises
FROM country 
GROUP BY country.governmentform 
ORDER BY COUNT(country.governmentform) DESC;

-- 6. Los nombres de los continentes con sus respectivas superficies ordenados de forma descendentes por superficie
SELECT DISTINCT country.continent AS continentes, SUM(country.surfacearea) AS Superficie 
FROM country 
GROUP BY country.continent
ORDER BY SUM(country.surfacearea) DESC;

-- 7. Los continentes y la cantidad de paises que los componen de aquellos continentes con mas de 15 paıses Idem g) pero
-- que los paıses que se tengan en cuenta tengan una poblacion de mas de 20 millones de personas
SELECT DISTINCT country.continent AS continentes, COUNT(country.name) AS Cantidad_paises 
FROM country
WHERE country.population > 20000000
GROUP BY country.continent
HAVING COUNT(country.name) > 15
