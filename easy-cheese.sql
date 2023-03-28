DROP DATABASE IF EXISTS easy-cheese;
CREATE DATABASE easy-cheese;

CREATE TABLE customers (
    customer_id     INT             AUTO_INCREMENT  PRIMARY KEY,
    name            VARCHAR(20)     NOT NULL,
    address         VARCHAR(100),
    email_address   VARCHAR(50)     NOT NULL,
    phone_number    VARCHAR(15)     NOT NULL
);

CREATE TABLE products (
    product_id      INT             AUTO_INCREMENT      PRIMARY KEY,
    vendor_id       INT             NOT NULL,
    qty             INT             NOT NULL,
    price           DECIMAL(9,2)    NOT NULL
);

create table invoices (
    invoice_id      INT             AUTO_INCREMENT      PRIMARY KEY,
    customer_id     int             not null,
    invoice_cost    decimal(9,2)    not null,
    invoice_tax     decimal(9,2)    not null,
    invoice_total   decimal(9,2)    not null,
    date            datetime        not null
)

create tABLE invoice_line_items (
    invoice_id      int             not null,
    product_id      int             not null,
    qty             int             not null
);