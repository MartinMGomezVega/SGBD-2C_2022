-- Los ´ındices son estructuras de datos secundarias (o auxiliares) que permiten acceder a los datos de una tabla en menor tiempo.
-- La estructura de datos m´as popular para implementar ´ındices se denomina B-tree (Ver https://en.wikipedia.org/ wiki/B-tree).

-- 1. De acuerdo a la tabla “sitio” del ejercicio anterior, analizar qu´e deber´ıa devolver la siguiente consulta:
--     s e l e c t ∗
--     from s i t i o s1 , s i t i o s 2
--     where s 1 . c oun t r yc ode = s 2 . c oun t r yc ode
--     and s 1 . e n ti d a d l i k e ’ a %’ and s 2 . e n ti d a d l i k e ’ b %’
--     l i m i t 100

-- 2. En general los motores de bases de datos relacionales proveen funcionalidades para analizar c´omo se ejecuta una consulta (ver secci´on 14.1). 
-- Analizar la consulta anterior con EXPLAIN PLAN y luego ejecutarla.

-- 3. Crear un indice sobre la columna “countrycode” de la tabla “sitio” y repetir el an´alisis del punto 2

-- 4. Ejecutar la consulta




-- PUNTO 1: Se devuelven dos tablas. La primera condicion que se ejecuta es que el countrycode de la tabla1 (s1) sea igual al de la tabla2 (s2).
--          La segunda condicion es que el campo entidad de la primer tabla empiece con 'a'. Y la tercer condicion es que el campo entidad de la tabla 2 empiece con 'b'.
--          De todos los registros encontrados, se devuelven los primeros 100.

-- PUNTO 2
EXPLAIN select * from sitio s1, sitio s2 where s1.countrycode = s2.countrycode and s1.entidad like 'a%' and s2.entidad like 'b%' limit 100;
------------------------------------------------------------------------------
 Limit  (cost=0.00..4.13 rows=100 width=44)
   ->  Nested Loop  (cost=0.00..271.25 rows=6564 width=44)
         Join Filter: (s1.countrycode = s2.countrycode)
         ->  Seq Scan on sitio s1  (cost=0.00..38.54 rows=128 width=22)
               Filter: (entidad ~~ 'a%'::text)
         ->  Materialize  (cost=0.00..39.04 rows=101 width=22)
               ->  Seq Scan on sitio s2  (cost=0.00..38.54 rows=101 width=22)
                     Filter: (entidad ~~ 'b%'::text)

