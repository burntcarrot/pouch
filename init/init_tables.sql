CREATE TABLE "customers" (
  "id" SERIAL PRIMARY KEY,
  "full_name" varchar,
  "email" varchar,
  "phone" varchar
);

CREATE TABLE "payments" (
  "id" SERIAL PRIMARY KEY,
  "amount" float,
  "datetime" date,
  "method" int,
  "order_id" int,
  "customer_id" int
);

CREATE TABLE "address" (
  "customer_id" int,
  "order_id" int,
  "address" varchar,
  PRIMARY KEY ("customer_id", "order_id")
);

CREATE TABLE "orders" (
  "id" SERIAL PRIMARY KEY,
  "datetime" date,
  "status" int
);

CREATE TABLE "order_details" (
  "order_id" int,
  "menu_id" int,
  "quantity" int,
  "amount" float,
  PRIMARY KEY ("order_id", "menu_id")
);

CREATE TABLE "menu" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar,
  "price" float,
  "description" varchar
);

ALTER TABLE "payments" ADD FOREIGN KEY ("order_id") REFERENCES "orders" ("id");

ALTER TABLE "payments" ADD FOREIGN KEY ("customer_id") REFERENCES "customers" ("id");

ALTER TABLE "address" ADD FOREIGN KEY ("customer_id") REFERENCES "customers" ("id");

ALTER TABLE "address" ADD FOREIGN KEY ("order_id") REFERENCES "orders" ("id");

ALTER TABLE "order_details" ADD FOREIGN KEY ("order_id") REFERENCES "orders" ("id");

ALTER TABLE "order_details" ADD FOREIGN KEY ("menu_id") REFERENCES "menu" ("id");
