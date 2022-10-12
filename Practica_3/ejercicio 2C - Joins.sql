-- 1. Los paises y las lenguas de los paises de Oceania
SELECT country.name AS Nombre_Pais, countrylanguage.language AS Lenguas 
FROM country 
INNER JOIN countrylanguage ON countrycode = country.code 
WHERE country.continent = 'Oceania';


-- 2. Los paises y la cantidad de lenguas de los paises en los que se habla mas de una lengua (ordenar por cantidad de lenguas de forma descendente)
SELECT country.name AS Nombre_Pais, count(countrylanguage.language) AS Cantidad_de_lenguas
FROM country 
INNER JOIN countrylanguage ON countrylanguage.countrycode = country.code 
GROUP BY country.name 
HAVING count(countrylanguage.language) > 1 
ORDER BY count(countrylanguage.language) DESC;


-- 3. Las lenguas que se hablan en el continente mas pobre (sin considerar a Antarctica)
SELECT countrylanguage.language AS Lenguas 
FROM countrylanguage 
INNER JOIN country ON countrylanguage.countrycode = country.code 
WHERE continent = (
        SELECT continent 
        FROM country 
        WHERE continent NOT LIKE 'Antarctica' 
        GROUP BY continent 
        ORDER BY avg(gnp) 
        --LIMIT 1
    );


-- 4. Los nombres de los paıses y sus respectivas poblaciones calculadas de formas distintas: 1) de acuerdo al campo de la
-- tabla country y 2) como suma de las polaciones de sus ciudades correspondientes, ademas se pide calcular el porcentaje
-- de poblacion urbana (de las ciudades), ordenar por porcentaje de modo descendente
SELECT country.name AS Nombre_Pais, country.population AS Poblacion, sum(city.population) AS Poblacion_de_la_ciudad, (sum(city.population) * 100 / country.population) as Porcentaje 
FROM country 
INNER JOIN city ON city.countrycode = country.code
GROUP BY country.name, country.population;


