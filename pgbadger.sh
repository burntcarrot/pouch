sudo cp postgres-data/log/postgresql.log logs/postgresql.log

sudo cat logs/postgresql.log | docker run -i --rm matsuu/pgbadger - -o - -x html -d carroteats --prefix '%t [%p]: [%l-1] user=%u,db=%d,app=%a,client=%h ' > out.html
