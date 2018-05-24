#!/bin/bash


for x in {1..20};
    do
    psql -c "\copy despesas FROM '/home/raphael/Downloads/OneDrive-2018-05-17/arquivos_brutos (cópia)/output$x.csv' DELIMITER ';' csv;"
#\copy zip_codes FROM '/path/to/csv/ZIP_CODES.txt' DELIMITER ',' CSV

done
