DROP DATABASE IF EXISTS easy_cheese;
CREATE DATABASE easy_cheese;

USE easy_cheese;

CREATE TABLE customers (
    customer_id     INT             AUTO_INCREMENT      PRIMARY KEY,
    name            VARCHAR(20)     NOT NULL,
    address         VARCHAR(100),
    email_address   VARCHAR(50)     NOT NULL,
    phone_number    VARCHAR(15)     NOT NULL
);

CREATE TABLE products (
    product_id      INT             AUTO_INCREMENT      PRIMARY KEY,
    name            VARCHAR(20)     NOT NULL,
    product_desc    VARCHAR(100),
    vendor_id       INT             NOT NULL,
    qty             INT             NOT NULL,
    price           DECIMAL(9,2)    NOT NULL,
    FOREIGN 
);

CREATE TABLE invoices (
    invoice_id      INT             AUTO_INCREMENT      PRIMARY KEY,
    customer_id     INT             NOT NULL,
    date            DATETIME        NOT NULL,
CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE invoice_line_items (
    invoice_id      INT             NOT NULL,
    product_id      INT             NOT NULL,
    qty             INT             NOT NULL,
    CONSTRAINT invoice_product_pk PRIMARY KEY (invoice_id, product_id)
);


create table vendors (
    vendor_id       INT             AUTO_INCREMENT      PRIMARY KEY,
    vendor_name     VARCHAR(20)     NOT NULL
);
-- create views -- 

-- sample data --
INSERT INTO customers (name, address, email_address, phone_number)
VALUES  ("parker",  "45 address way",   "parwal@yahoo.com",     "XXX-XXX-1234"),
        ("dylan",   "16 address st",    "dylmer@gmail.com",     "XXX-XXX-4565"),
        ("josh",    "32 address ave",   "joshar@hotmail.ca",    "XXX-XXX-7895"),
        ("sheham",  "57 address cr",    "sheha@protom.lol",     "XXX-XXX-3698");

INSERT INTO products (name, product_desc, vendor_id, qty, price)
VALUES  ("brie",      "a soft disc of cheese",  1, 17, 10.99),
        ("cheddar",   "a sharp classic",        2, 50, 5.49),
        ("parmesian", "a hard italian cheese",  1, 10, 25.99);

INSERT INTO invoices (invoice_id, customer_id, invoice_cost, date)
VALUES  (1,3,287.76,"2023-03-27"),
        (2,4,54.23,"2023-01-20"),
        (3,2,44.12,"2000-08-19"),
        (4,2,776.12,"2020-12-25");


