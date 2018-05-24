#!/bin/bash
x=0
for file in /home/raphael/Downloads/OneDrive-2018-05-17/arquivos_brutos1/*;
    do
    iconv -f ISO-8859-15 -t UTF-8 < $file > /home/raphael/Downloads/OneDrive-2018-05-17/output$x.csv
        let x++
done
