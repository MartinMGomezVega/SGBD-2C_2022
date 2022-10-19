-- Se pide crear la siguiente tabla
-- Nombre: sitio
-- Campos:
--     • id: int (es el n´umero de orden que aparece en cada l´ınea de la archivo)/primary key
--     • entidad: varchar (1ra. parte del dominio: hasta el 1er. punto)
--     • tipo entidad: varchar (2da. parte del dominio)
--     • pa´ıs: varchar (3ra. parte dela dominio)
--     • countrycode: foreign key a country.code

CREATE TABLE sitio (
    id integer NOT NULL PRIMARY KEY,
    entidad text NOT NULL,
    tipo_entidad text NOT NULL,
    pais text NOT NULL,
    countrycode character(3) NOT NULL references country(code)
);