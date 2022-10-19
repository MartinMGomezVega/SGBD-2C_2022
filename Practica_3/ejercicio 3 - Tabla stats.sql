-- Crear la siguiente tabla de estad´ısticas (utilizando la informaci´on de las tablas importadas):
-- Nombre: stats
-- Campos:
--     • countrycode: primary key/forign key (tabla country)
--     • cant lenguas: cantidad de lenguas que se hablan en el pa´ıs
--     • pop urbana: cantidad total de habitantes en las ciudades del pa´ıs


CREATE TABLE stats(
    countrycode character(3) NOT NULL references country(code),
    cant_lenguas integer,
    pop_urbana integer NOT NULL,
    PRIMARY KEY(countrycode)
);

INSERT INTO stats (countrycode, pop_urbana) (SELECT country.code, sum(city.population) FROM country INNER JOIN city on country.code = city.countrycode GROUP BY country.code);

UPDATE stats 
SET cant_lenguas = subquery.cant_language
FROM (SELECT country.code as countrycode, count(countrylanguage.language) as cant_language FROM country INNER JOIN countrylanguage on countrylanguage.countrycode = country.code GROUP BY country.code) as subquery where stats.countrycode = subquery.countrycode;
