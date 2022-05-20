start-old:
	@docker build -t postgres-dev ./
	@docker run -d -p 5432:5432 postgres-dev
start:
	@docker-compose down
	@docker-compose up -d --force-recreate
start-rm:
	@docker-compose down
	@sudo rm -rf postgres-data/
	@docker-compose up -d --force-recreate
gen-seed:
	@python3 gen_seeds.py
start-seed:
	@sudo cp -r seeds/ postgres-data/seeds/
	@docker-compose down
	@docker-compose up -d --force-recreate
	@sleep 5
	@bash seed.sh
