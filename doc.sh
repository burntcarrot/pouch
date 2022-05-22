ip=$(ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')

tbls doc postgres://postgres:password@"${ip}":5432/carroteats?sslmode=disable

mv dbdoc/ docs/
