CREATE PROCEDURE insert_data()
LANGUAGE SQL
AS $$
CREATE TABLE country (
    code CHAR(2) PRIMARY KEY
);
CREATE TABLE gei (
    date DATE,
    value FLOAT(2, 1), -- is this right? 56.3 kinda thing.
    country_code CHAR(2),
    PRIMARY KEY (date, country_code),
    FOREIGN KEY(country_code) references country(code)
);
$$;