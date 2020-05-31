container_id=$(docker ps | tail -1 | cut -d " " -f 1)
docker exec -it $container_id psql -U myuser -d postgres -c "DROP DATABASE my_financial_data;"
docker exec -it $container_id psql -U myuser -d postgres -c "CREATE DATABASE my_financial_data;"