ip=$(ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')

docker run -d -e DATABASE_URL=postgresql://testuser:password@$ip:5432/carroteats -p 8080:8080 ankane/pghero
