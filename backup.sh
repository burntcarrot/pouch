docker exec -t postgres-dev-postgresql-1 pg_dumpall -c -U postgres > dumps/dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
