load_customers="$(<"loaders/load_customers.sql")"
load_payments="$(<"loaders/load_payments.sql")"
load_address="$(<"loaders/load_address.sql")"
load_orders="$(<"loaders/load_orders.sql")"
load_order_details="$(<"loaders/load_order_details.sql")"
load_menu="$(<"loaders/load_menu.sql")"
delete_data="$(<"loaders/delete.sql")"

# first delete all table data
docker exec -it postgres-dev-postgresql-1 psql -U postgres -d carroteats -c "${delete_data}"

# load data into tables
docker exec -it postgres-dev-postgresql-1 psql -U postgres -d carroteats -c "${load_customers}"
docker exec -it postgres-dev-postgresql-1 psql -U postgres -d carroteats -c "${load_orders}"
docker exec -it postgres-dev-postgresql-1 psql -U postgres -d carroteats -c "${load_menu}"
docker exec -it postgres-dev-postgresql-1 psql -U postgres -d carroteats -c "${load_payments}"
docker exec -it postgres-dev-postgresql-1 psql -U postgres -d carroteats -c "${load_order_details}"
docker exec -it postgres-dev-postgresql-1 psql -U postgres -d carroteats -c "${load_address}"

# -c '\copy order_details FROM "/var/lib/postgresql/data/order_details.csv" DELIMITER "," CSV HEADER;'
