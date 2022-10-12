-- 1¿Que hace la siguiente consulta?
select name , lifeexpectancy from country where lifeexpectancy = (select min (lifeexpectancy) from country);
-- Devuelve el pais con menos esperanza de vida en este caso es Zambia con una esperanda de vida de 37.2

-- 2  Nombre del pais y la expectativa de vida de el/los pa´ıses con mayor y menor expectativa de vida
SELECT country.name AS Nombre_Pais , country.lifeexpectancy AS Esperanza_de_vida 
FROM country 
WHERE lifeexpectancy = (SELECT MIN (country.lifeexpectancy) FROM country) -- Pais con minima esperanza de vida
    OR 
    lifeexpectancy = (SELECT MAX (country.lifeexpectancy) FROM country); -- Pais con mayor esperanza de vida

-- 3  Nombre de los paıses y año de independencia que pertenecen al continente del paıs que se independizo hace mas tiempo
SELECT country.name AS Nombre_Pais, country.indepyear AS Año_Independencia 
FROM country 
WHERE continent = (SELECT country.continent AS Continente FROM country WHERE indepyear = (SELECT MIN (country.indepyear) FROM country));

-- 4 Nombres de los continentes que no pertenencen al conjunto de los continentes mas pobres
SELECT DISTINCT country.continent AS Continente 
FROM country
WHERE country.continent IN 
    (
        SELECT country.continent AS Continente 
        FROM country 
        GROUP BY country.continent 
        ORDER BY sum(country.gnp) DESC 
    );
