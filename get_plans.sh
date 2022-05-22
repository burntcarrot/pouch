query_order_details_order_id="$(<"explain_queries/order_details_order_id.sql")"

docker exec -t postgres-dev-postgresql-1 psql -U postgres -d carroteats -qAtc "${query_order_details_order_id}" > plans/plan_order_details_order_id.json
