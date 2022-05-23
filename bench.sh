docker exec -t postgres-dev-postgresql-1 pgbench -U postgres -c 20 -j 4 -T 60 -N carroteats > bench_results.txt
