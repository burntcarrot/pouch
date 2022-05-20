# pouch

My "hacky" way to setup PostgreSQL with mock data.

## Features

- Fuss-free Docker-based setup (Docker Compose)
- Table creation (init scripts)
- Seed generation through `faker` and Python
- Seeding PostgreSQL database through generated seeds and bash script (`seed.sh`)
- Loaders for loading csv data to PostgreSQL database
- Automatic data removal through `TRUNCATE TABLE` and delete script
