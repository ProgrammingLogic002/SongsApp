#!/bin/bash
echo "Iniciando importación de datos a songsapp_db..."

for file in /docker-entrypoint-initdb.d/*.json; do
    filename=$(basename "$file" .json)
    collection="${filename#songsapp_db.}"

    echo "Importando colección: $collection desde $file"
    mongoimport --db songsapp_db --collection "$collection" --file "$file" --jsonArray
done

echo "¡Importación terminada!"